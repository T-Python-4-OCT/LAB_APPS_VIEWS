from django.shortcuts import render

import random
import string
from django.http import HttpRequest, HttpResponse


def home_view(request: HttpRequest):
    return HttpResponse(
        "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    )


def about_view(request: HttpRequest):
    return HttpResponse(
        "Welcome to CarsRental! We provide a wide selection of reliable, well-maintained vehicles at competitive daily and weekly rates to make every trip smooth and comfortable."
    )


def password_generator_view(request: HttpRequest):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(characters, k=10))
    return HttpResponse(password)