import requests

# Replace these with your actual API keys
GOOGLE_API_KEY = 'AIzaSyC1OPBdF18AdTm9lTUjeXF-tZpJvdkAP50'
YOUTUBE_API_KEY = 'AIzaSyDbSCu3VjTPVTS89Nz0K-fK7Jn4SLcUc1o'
SEARCH_ENGINE_ID = '454edfcb47c2e4a9b'

def search_youtube_for_city(city_name):
    """Search YouTube for the first video related to the city."""
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': city_name,
        'type': 'video',
        'key': YOUTUBE_API_KEY,
        'maxResults': 1  # Only request the first search result
    }
    response = requests.get(search_url, params=params)
    return response.json()

def main():
    city_name = input("Enter the city name to explore: ")
    print(f"Searching for a video about {city_name}...\n")

    # YouTube search for the first city video
    youtube_results = search_youtube_for_city(city_name)
    if youtube_results.get('items'):
        item = youtube_results['items'][0]  # Get the first video result
        video_title = item['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        print(f"Found video: {video_title}\nURL: {video_url}\n")
    else:
        print("No videos found.")

if __name__ == '__main__':
    main()
