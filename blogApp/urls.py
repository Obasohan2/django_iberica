from django.urls import path
from . import views
from .views import PostDetail, PostLikeView


urlpatterns = [
    path('category/<int:category_id>/', views.category_post, name='category_post'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/like/<slug:slug>/', views.PostLikeView.as_view(), name='post_like'),
]
