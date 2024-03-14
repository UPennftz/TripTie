from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.views.generic import TemplateView

from .explorePage import search_youtube_for_city
from django.shortcuts import render
import requests
from tripapp.form import UserProfileForm, TripPlanForm
from tripapp.models import UserProfile, TripPlan, LikePost


class IndexView(View):
    def get(self, request):
        return render(request, 'tripapp/index.html')


# API key
YOUTUBE_API_KEY = 'AIzaSyDbSCu3VjTPVTS89Nz0K-fK7Jn4SLcUc1o'


def explore(request):
    return render(request, 'tripapp/explore.html')


def home(request):
    return render(request, 'tripapp/home.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'tripapp/about.html')


def index(request):
    return render(request, 'tripapp/index.html')


class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'gender': user_profile.gender,
                                'picture': user_profile.picture,
                                'bio': user_profile.bio, })

        return user, user_profile, form

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('tripapp:index'))

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'tripapp/profile.html', context_dict)


class EditProfileView(View):

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('tripapp:index'))

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'tripapp/edit_profile.html', context_dict)

    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'gender': user_profile.gender,
                                'picture': user_profile.picture,
                                'bio': user_profile.bio, })

        return user, user_profile, form

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('tripapp:index'))

        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('tripapp:profile',
                                    kwargs={'username': username}))
        else:
            print(form.errors)

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'tripapp/edit_profile.html', context_dict)


class MyTripPlansView(View):
    @method_decorator(login_required)
    def get(self, request, username):
        trip_plans = TripPlan.objects.filter(user=request.user).order_by('-start_date')

        return render(request, 'tripapp/my_trip_plans.html', {'trip_plans': trip_plans})


class MyLikesView(View):
    @method_decorator(login_required)
    def get(self, request, username):
        liked_trip_plans = LikePost.objects.filter(user=request.user).select_related('trip_plan')

        # Extract the trip plans from the likes
        trip_plans = [like.trip_plan for like in liked_trip_plans]

        context = {
            'trip_plans': trip_plans,
            'user': request.user,
        }

        return render(request, 'tripapp/my_likes.html', context)


class AddPlan(View):
    @method_decorator(login_required)
    def post(self, request, username):
        form = TripPlanForm(request.POST, request.FILES)
        context = {
            'username': username,
        }
        if form.is_valid():
            trip_plan = form.save(commit=False)
            trip_plan.user = request.user
            trip_plan.save()
            return render(request, 'tripapp/success.html')

        context = {
            'form': form,
            'username': username,
        }
        return render(request, 'tripapp/add_plan.html', context)

    @method_decorator(login_required)
    def get(self, request, username):
        context = {
            'username': username,
        }
        return render(request, 'tripapp/add_plan.html', context)


class SuccessView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'tripapp/success.html')


class WeatherView(View):
    def get(self, request):
        return render(request, 'tripapp/weather.html')


def myposts(request):
    return render(request, 'tripapp/myposts.html')


def messages(request):
    return render(request, 'tripapp/messages.html')


def explore_view(request):
    return render(request, 'tripapp/explore.html')


def explore(request):
    return render(request, 'tripapp/explore.html')


# def search_youtube(request):
# city_name = 'New York'
def search_youtube_for_city(request):
    city_name = request.GET.get('city', 'New York')

    search_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': city_name,
        'type': 'video',
        'key': YOUTUBE_API_KEY,
        'maxResults': 5
    }
    response = requests.get(search_url, params=params)
    videos = response.json().get('items', [])
    return JsonResponse(videos, safe=False)
