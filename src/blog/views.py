import os
from typing import Any

from django import http
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpRequest, HttpResponse
from django.urls import reverse
from django.core.paginator import (Paginator, 
                                   EmptyPage, 
                                   PageNotAnInteger)
from django.views import View
from django.views.generic import ListView, TemplateView
from django.core.mail import send_mail

from .forms import EmailPostForm
from .models import Post


def post_list(request):

    post_list = Post.published.all()

    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post/list.html', {'posts': posts})


class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    # we could use 'model = Post' that would be an eq of 'queryset = Post.models.all()'
    context_object_name = 'posts'
    # object_list by default

    paginate_by = 3
    

    template_name = 'post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug = post,
                             publish__year = year,
                             publish__month = month,
                             publish__day = day)
    return render(request, 'post/post_detail.html', {'post': post})

# now i wanna change this View to understand class-based views better


def share_post_by_email_view(request, post_id):
    post = get_object_or_404(Post,
                                    id=post_id,
                                    status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)  
        if form.is_valid():
            cd = form.cleaned_data # validated data are keeping in this field
            sent = send_post(post, cd, request)
    else:
        form = EmailPostForm()

    context = {
        'post': post,
        'form': form,
        'sent': sent
    }
    return render(request, 'post/share_post_by_email_form.html', context)


def send_post(post: Post, form_data, request: HttpRequest) -> True:
    '''returns True if mail was sent successfuly'''
    post_url = request.build_absolute_uri(
            post.get_absolute_url()) # to get full link
    subject = f"{form_data['name']} recommends you read " f"{post.title}"
    message = f"Read {post.title} at {post_url}\n\n" \
    f"{form_data['name']}\'s comments: {form_data['comments']}"

    send_mail(subject, message, 'adessergm@gmail.com',
    [form_data['to']])
    return True
        
        

