
from django.urls import path, include
from . import views
urlpatterns = [
    path(r'', views.blog_detail, name='blog_url'),
    path(r'<str:post_slug>', views.post_detail, name='post_detail_url'),
    path(r'<str:post_slug>/add_comment/', views.add_comment, name='add_comment_url'),
    path(r'category/<str:category_slug>/', views.category_detail, name='category_detail_url'),
]
