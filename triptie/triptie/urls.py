from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from tripapp import views  # Ensure you have home and explore_view defined here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),  # Homepage handled by IndexView
    path('tripapp/', include('tripapp.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('home/', views.home, name='home'),  # Path for the homepage view if different from IndexView
    path('weather/', views.WeatherView.as_view, name='weather'),  # Path for the homepage view if different from IndexView

    path('explore/', views.explore_view, name='explore'),  # Path for the explore view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
