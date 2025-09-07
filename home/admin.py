# models.py
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
        logo = models.ImageField(upload_to='restaurant_logos', blank=True, null=True)
            # Add other fields as needed