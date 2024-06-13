from django.shortcuts import render, HttpResponse
from .models import WeatherInfo

def display(request):
    return render(request, "home.html")

def weather(request):
    conditions = WeatherInfo.objects.all()
    return render(request, "weather.html", {"Forecast": conditions})