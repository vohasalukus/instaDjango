from django.shortcuts import render, get_object_or_404, redirect
from .forms import CategoryForm, PostForm, CommentForm
from .models import Category, Author, Post, Comment
from django.contrib.auth import logout


def category_list(request):
    post = Post.objects.all()
    sliced_post = post[:5]
    return render(
        request=request,
        template_name='insta_app/main_page.html',
        context={
            'categories': Category.objects.all(),
            'last_posts': sliced_post,
            'authors': Author.objects.all(),
        }
    )


def filter_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts_category.all()
    return render(
        request=request,
        template_name='insta_app/category.html',
        context={
            'category': category,
            'posts': posts,
        }
    )


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    return render(
        request=request,
        template_name='insta_app/add_category.html',
        context={'form': CategoryForm()}
    )


def filter_author(request, slug):
    author = get_object_or_404(Author, slug=slug)
    posts = author.posts_author.all()
    return render(
        request=request,
        template_name='insta_app/authors.html',
        context={
            'author': author,
            'posts': posts,
        }
    )


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    return render(
        request=request,
        template_name='insta_app/add_post.html',
        context={'form': PostForm()}
    )


def add_comm(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    return render(
        request=request,
        template_name='insta_app/add_comm.html',
        context={'form': CommentForm()}
    )


def exit(request):
    logout(request)
    return redirect('welcome')


