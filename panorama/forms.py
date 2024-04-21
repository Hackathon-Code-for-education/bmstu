from django import forms
from django.contrib.auth.models import User

from panorama.models import Profile, University


class SettingsForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "col-9 pole_for_log"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "col-9 pole_for_log"}))
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={"class": "col-9 pole_for_log"}))
    date = forms.DateField(label="Дата рождения",  widget=forms.DateInput(attrs={"class": "col-9 pole_for_log"}))
    education = forms.ChoiceField(label="Образование", choices=Profile.education_choices, widget=forms.Select(attrs={"class": "col-9 pole_for_log"}))
    # user_type = forms.ChoiceField(label="Тип пользователя", choices=Profile.user_type_choises, widget=forms.Select(attrs={"class": "col-9 pole_for_log"}))

    image = forms.ImageField(required=False, label="Загрузка аватара", widget=forms.FileInput(attrs={"class": "col-9"}))


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "col-9 pole_for_log"}))
    email = forms.EmailField(label="Почта", widget=forms.EmailInput(attrs={"class": "col-9 pole_for_log"}))
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={"class": "col-9 pole_for_log"}))
    date = forms.DateField(label="Дата рождения",  widget=forms.DateInput(attrs={"class": "col-9 pole_for_log"}))
    education = forms.ChoiceField(label="Образование", choices=Profile.education_choices, widget=forms.Select(attrs={"class": "col-9 pole_for_log"}))
    user_type = forms.ChoiceField(label="Тип пользователя", choices=Profile.user_type_choises, widget=forms.Select(attrs={"class": "col-9 pole_for_log"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "col-9 pole_for_log"}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={"class": "col-9 pole_for_log"}))

    image = forms.ImageField(required=True, label="Загрузка аватара", widget=forms.FileInput(attrs={"class": "col-9"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "col-9 pole_for_log"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "col-9 pole_for_log"}))



class AddReviewForm(forms.Form):
    review = forms.CharField(widget=forms.Textarea(attrs={"class": "col-9 pole_for_question", "placeholder": "Введи здесь свой отзыв"}))


class AddPanoramaForm(forms.Form):
    title = forms.CharField(max_length=50, label="Название маршрута", widget=forms.TextInput(attrs={"class": "col-9 pole_for_log"}))
    file = forms.FileField(required=True, label="Загрузка панорамы", widget=forms.FileInput(attrs={"class": "col-9"}))


class AddUniversityForm(forms.Form):
    representer = forms.CharField(max_length=50, label="Логин представителя", widget=forms.TextInput(attrs={"class": "col-9 pole_for_log"}))
    name = forms.CharField(max_length=50, label="Название организации", widget=forms.TextInput(attrs={"class": "col-9 pole_for_log"}))
    image = forms.ImageField(required=True, label="Загрузка обложки", widget=forms.FileInput(attrs={"class": "col-9"}))
    phone = forms.CharField(max_length=50, label="Телефон", widget=forms.TextInput(attrs={"class": "col-9 pole_for_log"}))
    description = forms.CharField(max_length=400, label="Описание организации", widget=forms.TextInput(attrs={"class": "col-9 pole_for_log"}))
    scan_file = forms.FileField(required=True, label="Свидетельство о государственной аккредитации", widget=forms.FileInput(attrs={"class": "col-9"}))


    class Meta:
        model = University
        fields = ('user', 'name', 'image', 'phoneNumber', )