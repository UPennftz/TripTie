 // initiating the process of fetching and displaying weather data on page load
 fetchWeatherInfo();


 // fetch weather data from API for a given latitude and longitude
 async function fetchWeather(lat, lon) {

     const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=auto`;

     try {
         const response = await fetch(url);
         if (!response.ok) {
             throw new Error('Failed to retrieve weather data');
         }
         const data = await response.json();
         return data;
     } catch (error) {
         console.error('Error fetching weather data:', error);
         throw error;
     }
 }



 // retrieves the geographical coordinates for a given city name
 async function getCoordinatesForCity(city) {
     const url = `https://nominatim.openstreetmap.org/search?city=${encodeURIComponent(city)}&format=json&limit=1`;

     try {
         const response = await fetch(url);
         if (!response.ok) {
             throw new Error('Failed to retrieve location data');
         }
         const data = await response.json();
         if (data.length === 0) {
             throw new Error('City not found');
         }
         // Extracting additional info from the response
         const latitude = data[0].lat;
         const longitude = data[0].lon;
         const region = data[0].state || ''; // 'state' might be a good proxy for region
         const country = data[0].country || '';
         return { latitude, longitude, city: city, region, country }; // Including city as it's not directly returned
     } catch (error) {
         console.error('Error fetching location data:', error);
         throw error;
     }
}




 // clears any previous weather information displayed for other days.
 function clearOtherDaysWeather() {
     const otherDaysBox = document.querySelector('.weather-box:last-child');
     otherDaysBox.innerHTML = '<h2>Other day temperature</h2>';
 }



 // fetch location, updates the display with the current location, fetch the weather data
 async function fetchWeatherInfo() {
     try {
         // Get location data from ipinfo.io
         const ipinfoResponse = await fetch('https://ipinfo.io?token=6732adc15fee27');
         const ipinfoData = await ipinfoResponse.json();
         // Update the location header with the retrieved location
         updateLocationDisplay(ipinfoData.city, ipinfoData.region, ipinfoData.country);
         const [lat, lon] = ipinfoData.loc.split(',');
         // Fetch both current weather and the forecast
         const weatherData = await fetchWeather(lat, lon);
         // Update the UI with the weather data
         updateWeatherUI(weatherData);
     } catch (error) {
         console.error("Failed to fetch weather data:", error);
         alert('Failed to fetch weather data. Please try again later.');
     }
 }



 // updates the page's header (<h1>) with the provided city, region, and country information
 function updateLocationDisplay(city, region, country) {
     const header = document.querySelector('header h1');
     let locationDisplay = city;
     if (region) locationDisplay += `, ${region}`;
     if (country) locationDisplay += `, ${country}`;
     header.textContent = `Location: ${locationDisplay}`;
 }




 // takes the weather data and updates the web page's content
 function updateWeatherUI(data) {
     const weatherContainer = document.getElementById('weather-container');
     const currentWeatherBox = weatherContainer.children[0];
     const otherDaysBox = weatherContainer.children[1];
     updateBackgroundVideo(data.current_weather.temperature);

     // Update current weather
     // Convert weather code to description
     const weatherDescriptions = {
         0: 'Clear sky',
         1: 'Mainly clear',
         2: 'Partly cloudy',
         3: 'Overcast',
     };
     const weatherDescription = weatherDescriptions[data.current_weather.weathercode] || 'Not available';

     // Format the time to a more readable format
     const weatherTime = new Date(data.current_weather.time);
     const timeString = weatherTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true });

     currentWeatherBox.innerHTML = `
         <h2>Current Weather:</h2>
         <p>Weather: ${weatherDescription}</p>
         <p>Temperature: ${data.current_weather.temperature}°C</p>
         <p>Time: ${timeString}</p>
     `;

     

     // Update other days' weather info
     let otherDaysHTML = '<h2>Other day temperature</h2>';
     if (data.daily && data.daily.time) {
         for (let i = 0; i < data.daily.time.length; i++) {
             const date = new Date(data.daily.time[i]);
             const dayName = date.toLocaleDateString('en-US', { weekday: 'long' });
             const maxTemp = data.daily.temperature_2m_max[i];
             const minTemp = data.daily.temperature_2m_min[i];

             otherDaysHTML += `
                 <p>${dayName}: Max: ${maxTemp}°C, Min: ${minTemp}°C</p>
             `;
         }
     }
     otherDaysBox.innerHTML = otherDaysHTML;
 }



 document.addEventListener('DOMContentLoaded', () => {
     const searchButton = document.getElementById('searchButton');
     searchButton.addEventListener('click', async () => {
         const cityInput = document.getElementById('cityName').value.trim();
         if (cityInput) {
             try {
                 const locationInfo = await getCoordinatesForCity(cityInput);
                 if (locationInfo) {
                     // Fetch the weather using the obtained coordinates
                     const weatherData = await fetchWeather(locationInfo.latitude, locationInfo.longitude);
                     // Update the location display with the fetched location data
                     updateLocationDisplay(locationInfo.city, locationInfo.region, locationInfo.country);
                     // Update the UI with the fetched weather data
                     updateWeatherUI(weatherData);
                 } else {
                     alert('Coordinates not found for the city.');
                 }
             } catch (error) {
                 console.error('Error:', error);
                 alert('Failed to fetch weather information. Please try again...');
             }
         } else {
             alert('Please enter a city name.');
         }
     });
 });

let temperature = data.current_weather.temperature;


function updateBackgroundVideo(temperature) {
const videoElement = document.getElementById('backgroundVideo');
let videoSource;

if (temperature <= 0) {
 videoSource = "{% static 'media/cold.mp4' %}";
} else if (temperature <= 15) {
 videoSource = "{% static 'media/mild.mp4' %}";
} 
else if (temperature <= 20) {
 videoSource = "{% static 'media/warm.mp4' %}";
} else if (temperature <= 27) {
 videoSource = "{% static 'media/hot.mp4' %}";
} else {
 videoSource = "{% static 'media/default.mp4' %}";
}

videoElement.src = videoSource;
videoElement.play().catch(e => console.error("Failed to play video", e));
}

