from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
from datetime import timedelta

STATUS = (
    ("Draft", "Draft"),
    ("Published", "Published"),
)


# ===============================
# CATEGORY MODEL
# ===============================

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name


# ===============================
# POST MODEL
# ===============================

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blogApp_posts"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    content = models.TextField()
    excerpt = models.TextField(blank=True)

    featured_image = CloudinaryField("image", blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Draft"
    )

    is_featured = models.BooleanField(default=False)

    featured_until = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Automatically expires 24 hours after being featured"
    )

    likes = models.ManyToManyField(
        User,
        related_name="myblogpost_like",
        blank=True
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        """
        Automatically set featured_until to 24 hours
        when a post is marked as featured.
        """
        if self.is_featured:
            if not self.featured_until or self.featured_until <= timezone.now():
                self.featured_until = timezone.now() + timedelta(hours=24)
        else:
            self.featured_until = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


# ===============================
# COMMENT MODEL
# ===============================

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()

    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
