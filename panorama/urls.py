from django.contrib.auth.decorators import login_required
from django.template.defaulttags import url
from django.urls import path

from panorama import views

urlpatterns = [
    path('', views.index, name='index'),
]
