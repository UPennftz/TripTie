import requests
# API Key test
YOUTUBE_API_KEY = 'AIzaSyDbSCu3VjTPVTS89Nz0K-fK7Jn4SLcUc1o'
city_name = 'London'
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

for video in videos:
    print(video['snippet']['title'])
