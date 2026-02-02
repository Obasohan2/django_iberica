from django.urls import path
from . import views
from .views import PostDetailView, CreatePostView, PostLikeView, PostEditView, PostDeleteView


urlpatterns = [
    path('category/post/create/', CreatePostView.as_view(), name='post_create'),
    path('category/<int:category_id>/', views.category_post, name='category_post'),
    path('category/post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/like/<slug:slug>/', PostLikeView.as_view(), name='post_like'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]