from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('posts/', views.posts, name='posts'),
    path('posts/add/', views.add_post, name='add_post'),
    path('posts/edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('posts/delete/<int:pk>/', views.delete_post, name='delete_post'),
]