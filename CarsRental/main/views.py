import random
import string

from django.shortcuts import render
from django.http import HttpResponse , HttpRequest

def home_view(request: HttpRequest):
    return HttpResponse(
        "Hello World, This is my new HOME for Car Rentals Website ! "
        "we're excited to welcome you here."
    )


def about_view(request: HttpRequest):
    return HttpResponse("A simple paragraph about Car Rentals.")


def password_view(request: HttpRequest):
    length = 10
    chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    all_chars = string.ascii_letters + string.digits + string.punctuation
    chars += [random.choice(all_chars) for _ in range(length - len(chars))]
    random.shuffle(chars)
    return HttpResponse("".join(chars))
