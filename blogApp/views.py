from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

# Local app imports
from .models import Post, Category
from .forms import RegistrationForm, PostForm
from django.template.defaultfilters import slugify   # Import slugify to generate slugs from titles


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


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required
def posts(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
        }
    return render(request, 'blogApp/posts.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save() # Save the post first to generate an ID for slugging
            
            # Automatically generate slug from title
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id) # Ensure slug is unique by appending post ID
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'blogApp/add_post.html', context)


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()            
            return redirect('post_detail', post_id=post.pk)  # Or 'home' if you don't have detail view
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'blogApp/edit_post.html', context)


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        # Ensure only the author can delete the post
        post.delete()
    return redirect('posts')