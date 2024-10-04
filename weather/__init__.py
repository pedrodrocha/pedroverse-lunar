import urllib3
import json

class OpenWeatherService:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    def __init__(self: "OpenWeatherService", api_key: str) -> None:
        self.api_key = api_key
        self.http = urllib3.PoolManager()

    def get_city_weather(self: "OpenWeatherService", city: str) -> dict:
        url = f"{self.BASE_URL}?q={city}&appid={self.api_key}&units=metric"
        response = self.http.request('GET', url)
        return json.loads(response.data.decode('utf-8'))

class WeatherServiceFactory:
    @staticmethod
    def create(api_key: str) -> OpenWeatherService:
        return OpenWeatherService(api_key)