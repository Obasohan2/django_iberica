from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your comment here...'
            }
        ),
        label=''
    )

    class Meta:
        model = Comment
        fields = ('body',)


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
        attrs={'class': 'form-control'}
    )

    status = forms.Select(
        attrs={'class': 'form-control'}
    )

    featured_image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={'class': 'form-control-file'}
        )
    )

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'category',
            'featured_image',
            'status',
        )
