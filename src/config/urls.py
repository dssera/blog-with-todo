from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('todo_app.urls', namespace='todo_app')),
    path('', include('blog.urls')),
    path('todo/', include('todo_app.urls')),
    path('admin/', admin.site.urls),
]
