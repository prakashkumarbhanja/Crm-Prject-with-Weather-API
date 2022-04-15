from django.urls import path, include

from weather_api.views import Fetch_weather_details

urlpatterns = [
    path('fetch_weather_details/', Fetch_weather_details.as_view(), name='fetch_weather_details'),
    
]
