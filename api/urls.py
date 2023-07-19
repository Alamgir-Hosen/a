from django.urls import path
from api import views
urlpatterns = [
    path("dogs/", views.get_all_dogs, name="dogs"),
    path("breeds/", views.get_all_breeds, name="breeds"),
]