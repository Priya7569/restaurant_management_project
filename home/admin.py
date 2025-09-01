from django.shortcuts import render
from .models import RestaurantLocation

def home(request):
    try:
            restaurant_location = RestaurantLocation.objects.first()
                except RestaurantLocation.DoesNotExist:
                        restaurant_location = None

                            return render(request, 'home.html', {'restaurant_location': restaurant_location})