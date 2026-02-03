from django.urls import path
from . import views
from .views import (
    PostDetailView,
    PostLikeView,
    PostEditView,
    PostDeleteView,
)

urlpatterns = [
    # Create post (function-based)
    path(
        'category/post/create/',
        views.create_post,
        name='post_create'
    ),

    # Category posts
    path(
        'category/<int:category_id>/',
        views.category_post,
        name='category_post'
    ),

    # Post detail
    path(
        'category/post/<slug:slug>/',
        PostDetailView.as_view(),
        name='post_detail'
    ),

    # Like / Unlike
    path(
        'post/like/<slug:slug>/',
        PostLikeView.as_view(),
        name='post_like'
    ),

    # Edit post
    path(
        'post/<int:pk>/edit/',
        PostEditView.as_view(),
        name='post_edit'
    ),

    # Delete post
    path(
        'post/<int:pk>/delete/',
        PostDeleteView.as_view(),
        name='post_delete'
    ),
]
