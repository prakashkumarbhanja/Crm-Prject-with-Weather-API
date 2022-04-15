import json
import urllib.request

from django.shortcuts import render

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from weather_api.throttling import WeatherApiRateThrottle
from .task import send_weather_api_mail

# Create your views here.


class Pagination(LimitOffsetPagination):
     PAGE_SIZE= 10

class Fetch_weather_details(APIView):

    pagination_class = Pagination
    throttle_classes = [WeatherApiRateThrottle]

    def get(self, request):

        weather_api = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=749d5d4127007dc92f6d5b77a9716753").read()

        list_of_data = json.loads(weather_api)

        # send_weather_api_mail.delay("Weather Data", 'pkbhanja07@gmail.com', 'list_of_data', 'prakashbhanja9@gmail.com')

        return Response (list_of_data, status = 200)
