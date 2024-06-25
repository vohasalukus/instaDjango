from django import forms
from .models import Category, Post, Comment


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = 'name',


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'title', 'content', 'category', 'author',


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "post", "author", "content",
