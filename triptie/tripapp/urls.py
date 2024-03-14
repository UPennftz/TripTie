
from django.urls import path
from . import views

app_name = 'tripapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('edit_profile/<username>/', views.EditProfileView.as_view(), name='edit_profile'),
    path('my_trip_plans/<username>/', views.MyTripPlansView.as_view(), name='my_trip_plans'),
    path('my_likes/<username>/', views.MyLikesView.as_view(), name='my_likes'),
    path('add_plan/<username>', views.AddPlan.as_view(), name='add_plan'),
    path('success/',views.SuccessView.as_view(), name='success'),
    path('messages/', views.messages, name='messages'),
    path('explore/', views.explore, name='explore'),
    path('search_youtube/', views.search_youtube_for_city, name='search_youtube'),
    path('weather/', views.weather, name='weather'),
    path('search_youtube/', views.search_youtube_for_city, name='search_youtube'),
    path('weather/', views.weather, name='weather'),
]
