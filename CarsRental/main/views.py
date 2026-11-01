import random
import string
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.


def home_view(request:HttpRequest):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")


def about_view(request:HttpRequest):
    return HttpResponse("A simple paragraph about Car Rentals.")


def password_generate_view(request:HttpRequest):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    password += random.choices(characters, k=10 - len(password))
    random.shuffle(password)

    return HttpResponse("".join(password))
