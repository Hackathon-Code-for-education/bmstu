from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login

from panorama.forms import RegisterForm
from panorama.models import *


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """

    univers = University.objects.all()

    print(univers)
    return render(
        request,
        'index.html',
        context={'universities': univers}
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
    if request.method == 'POST':
        user_form = RegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            user = User.objects.get(username=new_user.username)
            print(user)
            if request.FILES:
                print(1)
                # сдезь обработка файла должна быть
            login(request, new_user)
            return redirect(index)
        else:
            return render(
                request,
                'signup.html', context={"form": user_form}
            )

    form = RegisterForm()
    return render(
        request,
        'signup.html', context={"form": form}
    )


def settings(request):
    user_now = request.user

    return render(
        request,
        'settings.html', context={}
    )


def univer(request):
    """
    Функция отображения для домашней страницы сайта.
    """

    univers = University.objects.all()

    print(univers)
    return render(
        request,
        'index.html',
        context={'universities': univers}
    )