from django.shortcuts import redirect, render
from blogApp.models import Post, Category


def home(request):
    featured_posts = Post.objects.filter(is_featured=True, status='Published').order_by('updated_on')
    posts = Post.objects.filter(is_featured=False, status='Published')
    
    # Fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html', context)