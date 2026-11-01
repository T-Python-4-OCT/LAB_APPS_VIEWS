from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.crypto import get_random_string
import string
# Create your views here.

def home_view(request:HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request:HttpRequest):
    content = "Rent a car easily. Book online and go. Choose from economy to luxury, pay by the day, and enjoy a simple, flexible ride."
    return HttpResponse(content)

def password_generator(request:HttpRequest):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = get_random_string(length=10, allowed_chars=all_chars)
    return HttpResponse(password)
   