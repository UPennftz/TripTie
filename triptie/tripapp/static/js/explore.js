        function loadCityVideo(cityName, containerId) {
            fetch('/tripapp/search_youtube/?city=' + encodeURIComponent(cityName))
                .then(response => response.json())
                .then(data => {
                    const container = document.getElementById(containerId);
                    container.innerHTML = ''; // Clear previous content

                    if (data && data.length > 0) {
                        const video = data[0]; // Only take the first video
                        const videoFrame = document.createElement('iframe');
                        videoFrame.width = "100%";
                        videoFrame.height = "300";
                        videoFrame.src = `https://www.youtube.com/embed/${video.id.videoId}`;
                        videoFrame.frameBorder = "0";
                        videoFrame.allowFullscreen = true;
                        videoFrame.classList.add('video-iframe');

                        const videoTitle = document.createElement('h3');
                        videoTitle.textContent = video.snippet.title;
                        videoTitle.classList.add('video-title');

                        const videoDescription = document.createElement('p');
                        videoDescription.textContent = video.snippet.description;
                        videoDescription.classList.add('video-description');

                        const videoInfo = document.createElement('div');
                        videoInfo.classList.add('video-info');

                        videoInfo.appendChild(videoTitle);
                        videoInfo.appendChild(videoDescription);

                        const videoContainer = document.createElement('div');
                        videoContainer.classList.add('video-container');

                        videoContainer.appendChild(videoFrame);
                        videoContainer.appendChild(videoInfo);

                        container.appendChild(videoContainer);
                    } else {
                        container.textContent = 'No videos found for ' + cityName;
                    }
                })
                .catch(error => {
                    console.error('Error fetching data for ' + cityName + ':', error);
                });
        }

        document.getElementById('search-form').addEventListener('submit', function(e) {
            e.preventDefault();
            var cityName = document.getElementById('city-name').value + ' travel';
            loadCityVideo(cityName, 'youtube-videos'); // Add ' travel' only once
        });

        window.onload = function() {
            loadCityVideo('London travel', 'london-video');
            loadCityVideo('Paris travel', 'paris-video');
            loadCityVideo('Edinburgh travel', 'edinburgh-video');
        };