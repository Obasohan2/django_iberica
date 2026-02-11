from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DetailView

from blogApp.models import Post


# ===================== HOME =====================
def home(request):
    now = timezone.now()

    # ---------- AUTO-EXPIRE FEATURED POSTS ----------
    Post.objects.filter(
        is_featured=True,
        featured_until__isnull=False,
        featured_until__lt=now
    ).update(is_featured=False)

    # ---------- FEATURED POSTS ----------
    featured_posts = Post.objects.filter(
        is_featured=True,
        status="Published"
    ).order_by("-created_on")[:3]

    # ---------- REGULAR POSTS ----------
    posts = Post.objects.filter(
        is_featured=False,
        status="Published"
    )

    # ---------- PLACEHOLDERS (GRID BALANCE) ----------
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


# ===================== POST DETAIL =====================
class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Post.objects.filter(status="Published")
    