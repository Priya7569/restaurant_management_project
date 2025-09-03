from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
        address = models.CharField(max_length=255)
            city = models.CharField(max_length=100)
                state = models.CharField(max_length=50)
                    zip_code = models.CharField(max_length=10)
                        opening_hours = models.JSONField(default=dict)

                            def __str__(self):
                                    return self.name