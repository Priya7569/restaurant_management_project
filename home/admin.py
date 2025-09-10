# views.py
from django.shortcuts import render

def faq(request):
    faqs = [
            {"question": "What are your operating hours?", "answer": "We are open Monday to Saturday, 11 AM to 11 PM."},
                    {"question": "Do you offer delivery?", "answer": "Yes, we offer delivery through various partners in the city."},
                            {"question": "Can I book a table in advance?", "answer": "Yes, you can book a table by calling us or using our online booking system."},
                                    {"question": "Do you have vegetarian options?", "answer": "Yes, we have a variety of vegetarian dishes on our menu."},
                                        ]