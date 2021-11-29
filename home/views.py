from typing import ContextManager
from django.conf.urls import url
from django.shortcuts import render
import requests
import json
# Create your views here.
def home(request) :
    city = request.GET.get('city' , "delhi")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=164d8947c5bae61313dfe917b929f527'
    data = requests.get(url).json()
    
    payload = {
        'city' : data['name'],
    'weather' :data['weather'][0]['main'],
    'icon' : data['weather'][0]['icon'] ,
    'kelvin_temperature' : data['main']['temp'],
    'celcius_temperature' : int(data['main']['temp'] - 273),
    'humidity' : data['main']['humidity'] ,
    'pressure' : data['main']['pressure'],
    'description' : data['weather'][0]['description']
    }
   
    print(payload)
    return render(request , 'home.html', payload)
