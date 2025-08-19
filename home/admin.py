                                 <                                                <p>Price: {{ item.price }}</p>                              # views.py
                                 from rest_framework.response import Response
                                 from rest_framework.views import APIView
                                 
                                 class MenuView(APIView):
                                     def get(self, request):
                                             menu = [
                                                         {"name": "Paneer Butter Masala", "description": "A popular Indian dish", "price": 15.99},
                                                                     {"name": "Chicken Tikka Masala", "description": "A creamy and flavorful dish", "price": 14.99},
                                                                                 {"name": "Samosas", "description": "Crispy fried or baked pastries", "price": 6.99},
                                                                                             {"name": "Naan Bread", "description": "Leavened, butter-topped flatbread", "price": 3.99},
                                                                                                     ]
                                                                                                             return Response(menu)                                                                             r