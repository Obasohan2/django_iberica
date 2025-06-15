from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Category  # adjust based on your app structure
from .forms import RegistrationForm
# Create your views here.


def home(request):
    featured_posts = Post.objects.filter(is_featured=True, status='Published').order_by('updated_on')
    posts = Post.objects.filter(is_featured=False, status='Published')
    categories = Category.objects.all()  # <-- define categories here
    return render(request, 'index.html', {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts
    })


def category_posts(request, category_id):
    # fetch the posts that belongs to the category with the id category_id
    posts = Post.objects.filter(status='Published', category=category_id)

# Use try/except when we want to do some custom action if the category does not exists

    # try:
    # category = Category.objects.get(pk=category_id)

    # except:
    #     # redirect user to homepage
    #     return redirect('home')

# use get_object_or_404 when you want to show 404 error page if the category does not exist
    category = get_object_or_404(Category, pk=category_id)

    context = {
      'posts':posts,
      'category': category, 
      }
    return render(request, 'category_posts.html', context)


def search(request):
    # Your search logic here
    return render(request, 'blogApp/search.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # or wherever you want
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'blogApp/register.html', context)