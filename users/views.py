from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm


def welcome(request):
    return render(request=request, template_name='users_app/welcome.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
    return render(
        request=request,
        template_name='users_app/register.html',
        context=
        {'form': SignUpForm()})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print('user authenticated')
                login(request, user)
                return redirect('main_page')
            else:
                print('Username or password error')
                return redirect('register')
    return render(request=request, template_name='users_app/login.html',
                  context={'form': SignInForm()})


