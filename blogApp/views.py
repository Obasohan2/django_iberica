from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .models import Post, Category, Comment
from django.db.models import Q


def category_post(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Post.objects.filter(status='Published', category=category_id)
    # Use try/except when we want to do some custom action if the category does not exists
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect the user to homepage
    #     return redirect('home')
    
    # Use get_object_or_404 when you want to show 404 error page if the category does not exist
    category = get_object_or_404(Category, pk=category_id)
    
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'category_post.html', context)


# def Post(request, slug):
#     single_blog = get_object_or_404(Post, slug=slug, status='Published')
#     if request.method == 'POST':
#         comment = Comment()
#         comment.user = request.user
#         comment.blog = single_blog
#         comment.comment = request.POST['comment']
#         comment.save()
#         return HttpResponseRedirect(request.path_info)

#     # Comments
#     comments = Comment.objects.filter(blog=single_blog)
#     comment_count = comments.count()
    
#     context = {
#         'single_blog': single_blog,
#         'comments': comments,
#         'comment_count': comment_count,
#     }
#     return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    
    blogApp = Post.objects.filter(Q(title__icontains=keyword) | Q(excerpt__icontains=keyword) | Q(post_body__icontains=keyword), status='Published')
  
    context = {
        'blogApp': blogApp,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)


def blogApp(request, slug):
    single_blogApp = get_object_or_404(Post, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blogApp = single_blogApp
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    
    # Comments
    comments = Comment.objects.filter(blogApp=single_blogApp)
    comment_count = comments.count()
    
    context = {
        'single_blog': single_blogApp,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'blogs.html', context)
