from django.urls import path
from . import views

urlpatterns = [
    path("", views.display, name = "display"),
    path("weather/", views.weather, name = "weatherConditions")
]