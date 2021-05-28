import requests
from django.shortcuts import render
from .models import City
#Working with request
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=320c29ded5b96768afcdfa84fd09c631'
    city = 'Dallas'

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()
   

        city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],

        }
        weather_data.append(city_weather)
    
    print(weather_data)

    context = {'city_weather': city_weather}
    return render(request, 'weather/weather.html', context)
