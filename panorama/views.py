from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
# Create your views here.


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """

    return render(
        request,
        'index.html',
        context={}
    )

def login_user(request):
    """
    Функция отображения для домашней страницы сайта.
    """

    return render(
        request,
        'index.html',
        context={}
    )

def logout_user(request):
    logout(request)
    return redirect(login_user)

def signup(request):
    return render(
        request,
        'signup.html',
        context={}
    )

def settings(request):
    user_now = request.user

    return render(
        request,
        'settings.html', context={}
    )
