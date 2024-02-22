import requests
from flask import Flask, render_template, request

# Initialize Flask application
app = Flask(__name__)

# API keys
BING_API_KEY = 'BING_API_KEY'
YOUTUBE_API_KEY = 'API_KEY'

def search_bing_for_city(city_name):
    """Search Bing for information about the city."""
    url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {'Ocp-Apim-Subscription-Key': BING_API_KEY}
    params = {'q': city_name, 'count': 10, 'offset': 0, 'mkt': 'en-US'}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def search_youtube_for_city(city_name):
    """Search YouTube for videos related to the city."""
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': city_name,
        'type': 'video',
        'key': YOUTUBE_API_KEY,
        'maxResults': 10
    }
    response = requests.get(search_url, params=params)
    return response.json()

@app.route('/explore', methods=['GET', 'POST'])
def explore_page():
    if request.method == 'POST':
        city_name = request.form['city']
        # Use Bing API to search for city information (optional)
        bing_results = search_bing_for_city(city_name)
        # Use YouTube API to search for city videos
        youtube_results = search_youtube_for_city(city_name)
        return render_template('explore_results.html', city_name=city_name, youtube_results=youtube_results['items'])
    else:
        return render_template('explore.html')

if __name__ == '__main__':
    app.run(debug=True)
