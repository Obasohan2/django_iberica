from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'featured_image', 'excerpt', 'content', 'status', 'is_featured')
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']



