"""
URL configuration for iberica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from blogApp import views as PostsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Directs root path to blogApp
    path('summernote/', include('django_summernote.urls')),  # If using Summernote
    path('accounts/', include('allauth.urls')),  # If using django-allauth
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('category/', include('blogApp.urls')),
    path('blogApp/<slug:slug>/', PostsView.blogApp, name='blogApp'),
    # Search endpoint
    path('search/', PostsView.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
