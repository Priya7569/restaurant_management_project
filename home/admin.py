# views.py
from django.shortcuts import render
from .models import Cart

def homepage(request):
    cart_items = Cart.objects.filter(user=request.user)
        total_items = sum(item.quantity for item in cart_items)
            return render(request, 'homepage.html', {'total_items': total_items})