from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment, Category


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
        widget=SummernoteWidget()
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select category",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'category',
            'featured_image',
            'is_featured', 
            'status',
        )
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
