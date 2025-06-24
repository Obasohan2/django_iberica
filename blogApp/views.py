from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import UpdateView, DeleteView
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.text import slugify
from .forms import CommentForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q


def category_post(request, category_id):
    posts = Post.objects.filter(status='Published', category=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'category_posts.html', context)


class PostDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status='Published')
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status='Published')
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


def search(request):
    keyword = request.GET.get('keyword', '')
    results = []

    if keyword:
        results = Post.objects.filter(title__icontains=keyword)

    context = {
        'results': results,
        'keyword': keyword
    }
    return render(request, 'search.html', context)


class PostLikeView(View):  # Handles liking and unliking posts
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)  # Generate slug from title
            post.save()
            messages.success(request, "Your post was created successfully!")
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'  # reuse same form as create
    form_class = PostForm

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('home') 

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'  # Adjust path as needed
    success_url = reverse_lazy('home')  # or use get_success_url() method

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)