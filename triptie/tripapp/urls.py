
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('myposts/', views.myposts, name='myposts'),
    path('messages/', views.messages, name='messages'),
    path('explore/', views.explore, name='explore'),
    path('search_youtube/', views.search_youtube_for_city, name='search_youtube'),
    path('weather/', views.weather, name='weather'),
]
