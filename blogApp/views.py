from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
        
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# def search(request):
#     query = request.GET.get('q')
#     results = []
#     if query:
#         results = Post.objects.filter(title__icontains=query, status='Published')
#     return render(request, 'blogApp/search.html', {
#         'query': query,
#         'results': results
#     })


def search(request):
    keyword = request.GET.get('keyword', '')
    results = Post.objects.filter(title__icontains=keyword) if keyword else []
    return render(request, 'blogApp/search.html', {'results': results, 'keyword': keyword})