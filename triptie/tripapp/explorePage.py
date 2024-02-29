from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import requests

# API keys
YOUTUBE_API_KEY = 'AIzaSyDbSCu3VjTPVTS89Nz0K-fK7Jn4SLcUc1o'

@require_http_methods(["GET"])
def search_youtube_for_city(request):
    city_name = request.GET.get('city', '')
    max_results = 1
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': city_name,
        'type': 'video',
        'key': YOUTUBE_API_KEY,
        'maxResults': max_results
    }
    response = requests.get(search_url, params=params)
    videos = response.json().get('items', [])
    return JsonResponse({'videos': videos})  # Wrap the YouTube response in a dictionary under the 'videos' key



# Guide
# How to start Django：
# cd /Users/ftz/Desktop/itgroup/TripTie/triptie
# ls -l
# When shows manage.py is correct

# python manage.py runserver
# no respond 404 solve*
# cannot show correct data 200 solve*
# open the url below to open explore page
# http://127.0.0.1:8000/tripapp/explore/
