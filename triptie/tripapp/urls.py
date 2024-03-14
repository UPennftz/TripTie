"""triptie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from tripapp import views

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
]
