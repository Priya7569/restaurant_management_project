from django.db import models

class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
        city = models.CharField(max_length=100)
            state = models.CharField(max_length=50)
                zip_code = models.CharField(max_length=10)
                
                    def __str__(self):
                            return f"{self.address}, {self.city}, {self.state} {self.zip_code}"from django.conf import settings
from django.shortcuts import render

def home(request):
    restaurant_name = settings.RESTAURANT_NAME
        return render(request, 'home.html', {'restaurant_name': restaurant_name})