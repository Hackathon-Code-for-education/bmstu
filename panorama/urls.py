from django.contrib.auth.decorators import login_required
from django.template.defaulttags import url
from django.urls import path

from panorama import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout_user'),
    path('signup', views.signup, name='signup'),
    path('settings', views.settings, name='settings'),
    path('univer', views.univer, name='univer'),
]
