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
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
