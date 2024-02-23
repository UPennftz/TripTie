from django.shortcuts import render
from django.http import JsonResponse
import requests

# Replace with your actual YouTube API key
YOUTUBE_API_KEY = 'AIzaSyDbSCu3VjTPVTS89Nz0K-fK7Jn4SLcUc1o'

def explore(request):
    # This view just renders the page with the search box
    return render(request, 'tripapp/explore.html')

def search_youtube(request):
    # This view handles searching YouTube based on the city name query parameter
    city_name = request.GET.get('city', '')
    if city_name:
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
    else:
        return JsonResponse({'error': 'Missing city name'}, status=400)
