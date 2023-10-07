from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView
from . import views


app_name = 'blog'
'''
blog:post_list
blog:post_detail
'''
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>',
        views.post_detail, 
        name='post_detail'),
    path('share_post_by_email/<int:post_id>/', 
         views.share_post_by_email_view, 
         name='share_post_by_email'),
    # path('<int:post_id>/share/',
    #      views.share_post_by_email_view, name='post_share')
]