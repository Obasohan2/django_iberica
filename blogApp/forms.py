from django import forms
from .models import Post, Comment


# ===================== COMMENT FORM =====================

class CommentForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your comment here...'
            }
        ),
    )

    class Meta:
        model = Comment
        fields = ('body',)


# ===================== POST FORM =====================

class PostForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Post title'
            }
        )
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Write your post content here...'
            }
        )
    )

    category = forms.Select(
        attrs={
            'class': 'form-control'
        }
    )

    status = forms.Select(
        attrs={
            'class': 'form-control'
        }
    )

    featured_image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control-file'
            }
        )
    )

    is_featured = forms.BooleanField(
        required=False,
        label='Feature this post',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input'
            }
        )
    )

    featured_until = forms.DateTimeField(
        required=False,
        label='Feature until',
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'category',
            'featured_image',
            'is_featured',
            'featured_until',
            'status',
        )