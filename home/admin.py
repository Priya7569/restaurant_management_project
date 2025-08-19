                                 <                                                <p>Price: {{ item.price }}</p>                                                                                         # models.py
                                 from django.db import models
                                 from django.contrib.auth.models import User
                                 from .models import MenuItem
                                 
                                 class Order(models.Model):
                                     ORDER_STATUS_CHOICES = [
                                             ('pending', 'Pending'),
                                                     ('in_progress', 'In Progress'),
                                                             ('delivered', 'Delivered'),
                                                                     ('cancelled', 'Cancelled')
                                                                         ]
                                                                         
                                                                             customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
                                                                                 order_items = models.ManyToManyField(MenuItem, through='OrderItem')
                                                                                     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
                                                                                         order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
                                                                                             created_at = models.DateTimeField(auto_now_add=True)
                                                                                             
                                                                                                 def __str__(self):
                                                                                                         return f"Order {self.id} by {self.customer.username}"
                                                                                                         
                                                                                                         class OrderItem(models.Model):
                                                                                                             order = models.ForeignKey(Order, on_delete=models.CASCADE)
                                                                                                                 menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
                                                                                                                     quantity = models.IntegerField()
                                                                                                                     
                                                                                                                         def __str__(self):
                                                                                                                                 return f"{self.quantity} x {self.menu_item.name}"                                                                              r