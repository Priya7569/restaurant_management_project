from django.shortcuts import render
from .models import MenuItem

def home(request):
    query = request.GET.get('q')
        if query:
                menu_items = MenuItem.objects.filter(name__icontains=query)
                    else:
                            menu_items = MenuItem.objects.all()
                                return render(request, 'home.html', {'menu_items': menu_items, 'query': query})