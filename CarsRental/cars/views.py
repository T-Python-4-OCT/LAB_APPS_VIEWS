from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import random
import string


def home(request):
    return HttpResponse(
        "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    )


def about(request):
    return HttpResponse(
        "Our car rental service offers reliable and affordable vehicles "
        "to help customers travel comfortably and conveniently."
    )


def generate_password(request):
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = (
        random.choice(string.ascii_uppercase)
        + random.choice(string.ascii_lowercase)
        + random.choice(string.digits)
        + random.choice(string.punctuation)
        + ''.join(random.choice(characters) for _ in range(6))
    )

    password = ''.join(random.sample(password, len(password)))

    return HttpResponse(password)