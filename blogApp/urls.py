from django.urls import path
from . import views
from .views import (
    PostDetailView,
    PostLikeView,
    PostEditView,
    PostDeleteView,
)

urlpatterns = [
    path('post/create/', views.create_post, name='post_create'),

    # category
    path('category/<slug:slug>/', views.category_post, name='category_post'),


    # post detail
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),

    # like
    path('like/<slug:slug>/', PostLikeView.as_view(), name='post_like'),

    # edit / delete
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
    path('profile/', views.profile_view, name='profile'),
]

