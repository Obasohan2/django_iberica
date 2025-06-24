from django.urls import path
from . import views
from .views import PostDetail, PostLikeView, create_post, PostEditView, PostDeleteView


urlpatterns = [
    path('post/create/', create_post, name='post_create'), 
    path('category/<int:category_id>/', views.category_post, name='category_post'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/like/<slug:slug>/', views.PostLikeView.as_view(), name='post_like'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
