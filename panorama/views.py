
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login

from panorama.forms import RegisterForm, SettingsForm, LoginForm, AddReviewForm
from panorama.helpers import add_image_profile
from panorama.models import *
from django.http import HttpResponse


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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(index)
                else:
                    return HttpResponse('Disabled account')
            else:
                form.add_error('username', 'Invalid login or password')
    else:
        form = LoginForm()

    return render(
        request,
        'login.html', context={"form": form}
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
                add_image_profile(user, request)
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
    if request.method == "POST":
        form = SettingsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.get(username=user_now.username)
            # user.profile.image
            print(data)
            user.username = data["username"]
            user.first_name = data["first_name"]
            user.email = data["email"]
            user.save()
            if request.FILES:
                add_image_profile(user, request)


            return render(
                request,
                'settings.html', context={"form": form}
            )

        else:
            print(form.is_valid())

    user = User.objects.get(username=user_now.username)
    profile = Profile.objects.get(user=user.id)

    print(profile)

    form = SettingsForm(initial={'username': user.username, 'first_name': user.first_name,
                                 'email': user.email,
                                 'image': profile.image.url
                                 })
    # print(form)
    #form.set_values(user_now.username, user_now.email, user_now.first_name)


    return render(
        request,
        'settings.html', context={"form": form}
    )
def univer(request, univer_id):
    """
    Функция отображения для домашней страницы сайта.
    """
    item = University.objects.get(id=univer_id)


    try:
        if request.method == "POST":
            form = AddReviewForm(request.POST)
            if form.is_valid():
                if request.user.is_authenticated:
                    data = form.cleaned_data
                    item.reviews.create(text=data["review"], user=request.user)
                else:
                    form.add_error('review', "You must be logged in!")
                    return render(
                        request,
                        'university.html',
                        context={'item': item, 'form': form}
                    )
    except Exception as e:
        print(e)

    form = AddReviewForm()

    return render(
        request,
        'university.html',
        context={'item': item, 'form': form}
    )


def panorama(request, univer_id):

    univers = University.objects.all()

    print(univers)
    return render(
        request,
        'panorama.html',
        context={}
    )


def privacy_policy(request):
    return  render(
        request,
        'privacy_policy.html',
        context={}
    )


def administr_panorama(request):
    return  render(
        request,
        'admin/admin_univers.html',
        context={}
    )


def for_univers(request):
    return  render(
        request,
        'for_universities.html',
        context={}
    )