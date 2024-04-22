from django.contrib.auth.decorators import login_required
from django.template.defaulttags import url
from django.urls import path

from panorama import views
from panorama.models import Review, LikeDis

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout_user'),
    path('signup', views.signup, name='signup'),
    path('settings', views.settings, name='settings'),
    path('univer/<int:univer_id>', views.univer, name='univer'),
    path('univer/<int:univer_id>/panorama', views.panorama, name='panorama'),
    path('for_univers', views.for_univers, name='for_univers'),
    path('add_panorama', views.add_paorama, name='add_panorama'),
    path('add_univer', views.add_univer, name='add_univer'),
    path('chat', views.chat, name='chat'),

    path('privacy_policy', views.privacy_policy, name='policy'),
    path('admin_pan', views.administr_panorama, name='admin_pan'),


    path('api/answer/<int:id>/like/',
         login_required(views.VotesView.as_view(model=Review, vote_type=LikeDis.LIKE)),
         name='answer_like'),
    path('api/answer/<int:id>/dislike/',
         login_required(views.VotesView.as_view(model=Review, vote_type=LikeDis.DISLIKE)),
         name='answer_dislike'),

]
