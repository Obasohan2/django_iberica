from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
        
        
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'category', 'featured_image', 'excerpt', 'content', 'status', 'is_featured')
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'featured_image', 'status',)

