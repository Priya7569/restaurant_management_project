                            # models.py
                            from django.db import models
                            from django.contrib.auth.models import User
                            
                            class UserProfile(models.Model):
                                user = models.OneToOneField(User, on_delete=models.CASCADE)
                                    name = models.CharField(max_length=255)
                                        email = models.EmailField(unique=True)
                                            phone_number = models.CharField(max_length=20)
                                            
                                                def __str__(self):
                                                        return self.user.username                                                                                                   return render(request, 'menu.html', {'menu_items': menu_items})