from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
)
from django.views import View
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Q

from .models import Post, Category
from .forms import CommentForm, PostForm


# ===================== CATEGORY POSTS =====================

def category_post(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(
        status='Published',
        category=category
    )

    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'category_posts.html', context)


# ===================== POST DETAIL + COMMENTS =====================

class PostDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(
            Post,
            slug=slug,
            status='Published'
        )

        comments = post.comments.filter(
            approved=True
        ).order_by('-created_on')

        liked = False
        if request.user.is_authenticated:
            liked = post.likes.filter(id=request.user.id).exists()

        context = {
            'post': post,
            'comments': comments,
            'commented': False,
            'liked': liked,
            'comment_form': CommentForm(),
        }

        return render(request, 'post_detail.html', context)

    def post(self, request, slug, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(
                request,
                "You must be logged in to comment."
            )
            return redirect('account_login')

        post = get_object_or_404(
            Post,
            slug=slug,
            status='Published'
        )

        comments = post.comments.filter(
            approved=True
        ).order_by('-created_on')

        liked = post.likes.filter(
            id=request.user.id
        ).exists()

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.name = request.user.username
            comment.email = request.user.email
            comment.save()
            commented = True
        else:
            commented = False

        context = {
            'post': post,
            'comments': comments,
            'commented': commented,
            'liked': liked,
            'comment_form': comment_form,
        }

        return render(request, 'post_detail.html', context)


# ===================== SEARCH =====================

def search(request):
    keyword = request.GET.get('keyword', '').strip()
    results = []

    if keyword:
        results = Post.objects.filter(
            Q(title__icontains=keyword) |
            Q(content__icontains=keyword),
            status='Published'
        ).order_by('-created_on')

    context = {
        'results': results,
        'keyword': keyword,
    }

    return render(request, 'search.html', context)


# ===================== LIKE / UNLIKE =====================

class PostLikeView(View):

    def post(self, request, slug):
        if not request.user.is_authenticated:
            return redirect('account_login')

        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(
            reverse('post_detail', args=[slug])
        )


# ===================== CREATE POST =====================

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            base_slug = slugify(post.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            post.slug = slug
            post.save()

            messages.success(
                request,
                "Your post was created successfully!"
            )
            return redirect('home')
    else:
        form = PostForm()

    return render(
        request,
        'post_form.html',
        {'form': form}
    )


# ===================== EDIT POST =====================

class PostEditView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse(
            'post_detail',
            kwargs={'slug': self.object.slug}
        )


# ===================== DELETE POST =====================

class PostDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user == self.get_object().author
