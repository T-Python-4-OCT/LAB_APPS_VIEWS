from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string
# Create your views here.

def home_view(request: HttpRequest):
    return HttpResponse("Hello thier This my new HOME for car welcome you here")

def about_view(request: HttpRequest):
    return HttpResponse("A simple paragraph about car Rentals. ")

def password_view(request: HttpRequest):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(10))
    return HttpResponse(password) 