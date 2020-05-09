
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.BlogPageView.as_view(), name='blog_url'),
    path('<str:post_slug>/', views.PostDetailView.as_view(), name='post_detail_url'),
    path('<str:post_slug>/add_comment/', views.add_comment, name='add_comment_url'),
    path('category/<str:category_slug>/', views.CategoryDetailView.as_view(), name='category_detail_url'),
]
