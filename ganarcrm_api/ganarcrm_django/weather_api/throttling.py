
from rest_framework.throttling import UserRateThrottle

class WeatherApiRateThrottle(UserRateThrottle):
    scope = 'weather_api'