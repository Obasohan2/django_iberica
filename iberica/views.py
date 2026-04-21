from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DetailView

from blogApp.models import Post


# Home view
def home(request):
    now = timezone.now()

    # Expire featured posts past their display date
    Post.objects.filter(
        is_featured=True,
        featured_until__isnull=False,
        featured_until__lt=now
    ).update(is_featured=False)

    # Retrieve latest featured posts (max 3)
    featured_posts = Post.objects.filter(
        is_featured=True,
        status="Published"
    ).order_by("-created_on")[:3]

    # Retrieve non-featured published posts
    posts = Post.objects.filter(
        is_featured=False,
        status="Published"
    )

    # Determine placeholders for grid alignment
    remainder = posts.count() % 3
    placeholders = (3 - remainder) if remainder != 0 else 0

    return render(
        request,
        "home.html",
        {
            "featured_posts": featured_posts,
            "posts": posts,
            "placeholders": range(placeholders),
        }
    )


# Post detail view
class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        # Restrict to published posts only
        return Post.objects.filter(status="Published")