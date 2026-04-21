from django.urls import path
from . import views
from .views import (
    PostDetailView,
    PostLikeView,
    PostEditView,
    PostDeleteView,
)

urlpatterns = [
    # Create post
    path('post/create/', views.create_post, name='post_create'),

    # Category posts
    path('category/<slug:slug>/', views.category_post, name='category_post'),

    # Post detail
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),

    # Like / unlike post
    path('like/<slug:slug>/', PostLikeView.as_view(), name='post_like'),

    # Edit post
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),

    # Delete post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # User profile
    path('profile/', views.profile_view, name='profile'),
]