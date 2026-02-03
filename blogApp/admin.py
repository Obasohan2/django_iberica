from django.contrib import admin
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_on', 'updated_on')
    search_fields = ('category_name',)
    prepopulated_fields = {"slug": ("category_name",)}


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'image_preview',
        'status',
        'is_featured',
        'category',
        'author',
        'created_on',
    )

    list_editable = ('is_featured',)
    list_filter = ('status', 'created_on', 'category')
    search_fields = ('title', 'content', 'category__category_name')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.featured_image and obj.featured_image.url != "placeholder":
            return format_html(
                '<img src="{}" style="width: 80px; height: auto; border-radius: 4px;" />',
                obj.featured_image.url
            )
        return "No image"

    image_preview.short_description = "Image"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
