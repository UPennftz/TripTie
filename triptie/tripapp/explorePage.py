from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import requests

# API keys
YOUTUBE_API_KEY = 'AIzaSyDbSCu3VjTPVTS89Nz0K-fK7Jn4SLcUc1o'

@require_http_methods(["GET"])
def search_youtube_for_city(request):
    """Search YouTube for videos related to the city."""
    city_name = request.GET.get('city', '')
    max_results = 5
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
# cannot show correct data 200
# open the url like this
# http://127.0.0.1:8000/tripapp/explore/



# # API keys
# GOOGLE_API_KEY = 'AIzaSyC1OPBdF18AdTm9lTUjeXF-tZpJvdkAP50'
# YOUTUBE_API_KEY = 'AIzaSyDbSCu3VjTPVTS89Nz0K-fK7Jn4SLcUc1o'
# SEARCH_ENGINE_ID = '454edfcb47c2e4a9b'
#
# def search_youtube_for_city(city_name, max_results=5):
#     """Search YouTube for videos related to the city."""
#     search_url = 'https://www.googleapis.com/youtube/v3/search'
#     params = {
#         'part': 'snippet',
#         'q': city_name,
#         'type': 'video',
#         'key': YOUTUBE_API_KEY,
#         'maxResults': max_results  # The number of search results
#     }
#     response = requests.get(search_url, params=params)
#     return response.json()
#
# def main():
#     city_name = input("Enter the city name to explore: ")
#     print(f"Searching for videos about {city_name}...\n")
#
#     # YouTube search for city videos
#     youtube_results = search_youtube_for_city(city_name)
#     if youtube_results.get('items'):
#         for item in youtube_results['items']:
#             video_title = item['snippet']['title']
#             video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
#             print(f"Found video: {video_title}\nURL: {video_url}\n")
#     else:
#         print("No videos found.")
#
# if __name__ == '__main__':
#     main()
