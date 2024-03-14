
from django.urls import path
from . import views

app_name = 'tripapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('myposts/', views.myposts, name='myposts'),
    path('messages/', views.messages, name='messages'),
    path('explore/', views.explore, name='explore'),
    path('search_youtube/', views.search_youtube_for_city, name='search_youtube'),
    path('weather/', views.weather, name='weather'),
    path('search_youtube/', views.search_youtube_for_city, name='search_youtube'),
    path('weather/', views.weather, name='weather'),
]
