const menuToggle = document.querySelector('.toggle');
const showcase = document.querySelector('.showcase');

menuToggle.addEventListener('click', () => {
  menuToggle.classList.toggle('active');
  showcase.classList.toggle('active');
});

document.getElementById("Login | Register").addEventListener("click", function() {
  fetch('/popup/')
      .then(response => response.text())
      .then(html => {
          const popupWindow = window.open('', '_blank', 'width=600,height=400');
          popupWindow.document.write(html);
          popupWindow.document.close();
      })
      .catch(error => console.error('Error loading the popup content:', error));
});

function tweetShare() {
  window.open('https://twitter.com/intent/tweet?text=Check%20out%20this%20awesome%20website%21%20https%3A%2F%2Fexample.com%2F');
}

function shareOnFacebook() {
    var url = encodeURIComponent(window.location.href);
    window.open('https://www.facebook.com/sharer/sharer.php?u=' + url, '_blank');
}

function openForm(formName) {
  document.getElementById(formName).style.display = "block";
}

function closeForm() {
  document.getElementById("loginForm").style.display = "none";
  document.getElementById("registerForm").style.display = "none";
}
