from django.shortcuts import render
from django.http import JsonResponse
from .explorePage import search_youtube_for_city
from django.shortcuts import render
import requests

# API key
YOUTUBE_API_KEY = 'AIzaSyDbSCu3VjTPVTS89Nz0K-fK7Jn4SLcUc1o'

def explore(request):
    return render(request, 'tripapp/explore.html')

def explore_view(request):
    return render(request, 'tripapp/explore.html')

def home(request):
    return render(request, 'tripapp/home.html')

def about(request):
    return render(request, 'tripapp/about.html')

def index(request):
    return render(request, 'tripapp/index.html')

def login(request):
    return render(request, 'tripapp/login.html')

def weather(request):
    return render(request, 'tripapp/weather.html')

def profile(request):
    return render(request, 'tripapp/profile.html')

def myposts(request):
    return render(request, 'tripapp/myposts.html')

def messages(request):
    return render(request, 'tripapp/messages.html')

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

