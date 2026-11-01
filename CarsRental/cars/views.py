from django.shortcuts import render

from django.http import HttpResponse
import random
import string


def home(request):
    return HttpResponse(
        "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    )


def about(request):
    return HttpResponse("We are not the only car rental company, but we are the best!")


def password_generate(request):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(10))

    return HttpResponse(password)
