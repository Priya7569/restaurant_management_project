  # views.py
  from django.shortcuts import render
  from .models import MenuItem
  from django.db import DatabaseError
  
  def menu(request):
      try:
              menu_items = MenuItem.objects.all()
                      return render(request, 'menu.html', {'menu_items': menu_items})
                          except DatabaseError as e:
                                  # Log the error
                                          print(f"Database error: {e}")
                                                  # Return a user-friendly error message
                                                          return render(request, 'error.html', {'message': 'Failed to retrieve menu items due to a database error.'})
                                                              except Exception as e:
                                                                      # Log the error
                                                                              print(f"Unexpected error: {e}")
                                                                                      # Return a user-friendly error message
                                                                                              return render(request, 'error.html', {'message': 'An unexpected error occurred.'})                                                                                                                                                                                                                                                                                               <label for=                                                                                                                                return render(request, 'menu.html', {'menu_items': menu_items})