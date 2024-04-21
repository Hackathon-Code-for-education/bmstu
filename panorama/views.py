
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login

from panorama.forms import RegisterForm, SettingsForm, LoginForm, AddReviewForm, AddPanoramaForm, AddUniversityForm
from panorama.helpers import add_image_profile, add_zip_file, add_image_univer
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

            data = user_form.cleaned_data
            print(data)
            # {'username': 'qqq', 'first_name': 'qeee', 'email': 'eee@mail.ru',
            # 'date': datetime.date(2000, 10, 10), 'education': 'BG',
            # 'user_type': 'AB', 'password': '1234', 'password2': '1234', 'image': None}
            # qqq
            try:
                profile = Profile.objects.create(user = user, birth_date=data['date'],
                                              education=data['education'], user_type=data['user_type'])
            except Exception as e:
                print(e)

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
                                 'image': profile.image.url,
                                 'date': profile.birth_date
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
                    review = data["review"]
                    print(review)
                    # if check_review(review):
                    item.reviews.create(text=data["review"], user=request.user)
                    """
                    else:
                        form.add_error('review', "Такое нельзя писать здесь")
                    """
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
    verified = []
    on_moderate = []
    declined = []
    try:
        # University.objects.get_queryset()
        verified = University.objects.filter(check_type = "VF")
    except Exception as e:
        print(e)
    try:
        on_moderate = University.objects.filter(check_type = "MO")
    except Exception as e:
        print(e)
    try:
        declined = University.objects.filter(check_type = "DE")
    except Exception as e:
        print(e)


    univers = {
        'verified': verified,
        'on_moderate': on_moderate,
        'declined': declined
    }


    return  render(
        request,
        'admin/admin_univers.html',
        context={'univers': univers}
    )


def for_univers(request):
    return  render(
        request,
        'for_universities.html',
        context={}
    )

def add_paorama(request):
    form = AddPanoramaForm()

    user = request.user
    univer = University.objects.get(user=user)
    univer_id = univer.id
    # redirect(panorama, univer_id=univer_id)

    if request.method == "POST":
        form = AddPanoramaForm(request.POST, request.FILES)
        if form.is_valid():
            res=add_zip_file(request.user, form)
            file_url = res[1]
            print(file_url)
            print(res)
            user = request.user.is_staff
            univer = University.objects.get(user=user)
            univer_id = univer.id
            return redirect(panorama, univer_id=univer_id)
        else:
            print("nooooo")



    else:
        form = AddPanoramaForm()

    return  render(
        request,
        'add_panorama.html',
        context={'form': form}
    )



def add_univer(request):
    form = AddUniversityForm()
    user = request.user
    if request.method == "POST":
        form = AddUniversityForm(request.POST, request.FILES)
        if form.is_valid():
            # res=add_zip_file(request.user, form)
            # file_url = res[1]
            # print(file_url)

            data = form.cleaned_data

            representer = data['representer']

            name = data['name']

            image = data['image']

            phone = data['phone']

            description = data['description']

            scan_file = data['scan_file']

            new_univer = University()
            new_univer.user = user
            new_univer.name = name
            new_univer.phoneNumber = phone
            new_univer.description = description

            new_univer.check_type = University.on_moderate
            try:
                new_univer.save()

            except Exception as e:
                print(e)


            if image:
                add_image_univer(user,image)


            print(data)

            #new_user = form.sa
            # new_user.set_password(user_form.cleaned_data['password'])
            """
            new_user.save()
            user = User.objects.get(username=new_user.username)
            print(user)
            if request.FILES:
                add_image_profile(user, request)
            login(request, new_user)
            return redirect(index)
            data = form.cleaned_data
            print(data)
            """
            return redirect(index)
        else:
            print("nooooo")



    else:
        form = AddUniversityForm()

    return  render(
        request,
        'add_university.html',
        context={'form': form}
    )

def chat(request):
    return render(
        request,
        'chat.html',
        context={}
    )