from django.shortcuts import render
import secrets
import string

from django.http import HttpRequest, HttpResponse


def home_view(request: HttpRequest):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here.")


def about_view(request: HttpRequest):
    return HttpResponse("<p>CarsRental makes renting a car simple. Choose from economy cars, family SUVs and luxury models, pick your dates, and collect your car from the nearest branch. We offer daily, weekly and monthly plans with clear prices and no hidden fees.</p>")


def password_view(request: HttpRequest):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_chars = lower + upper + digits + symbols

    password = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    for i in range(6):
        password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)

    return HttpResponse("".join(password), content_type="text/plain")

# Create your views here.
