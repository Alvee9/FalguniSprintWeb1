from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('homepage', views.homepage, name='homepage'),
    path('nominate', views.nominate, name='nominate'),
    path('votepage', views.votepage, name='votepage'),
    path('vote', views.vote, name='vote'),
    path('result', views.result, name='result'),
    path('logout', views.logout, name='logout'), 
]