from django.contrib import admin
from .models import Post


# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']

    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    
    # it means that title.text will be the same with title.text
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']