from django.shortcuts import redirect, render
from blogApp.models import Post, Category
from django.views.generic import DetailView



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


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'post_detail.html'
#     context_object_name = 'post'
#     slug_field = 'slug'
#     slug_url_kwarg = 'slug'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    slug_field = 'slug'  # field on the model
    slug_url_kwarg = 'slug'  # parameter in the URL

    def get_queryset(self):
        return Post.objects.filter(status='Published')