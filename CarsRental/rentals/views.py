from django.shortcuts import render

import secrets
import string

from django.http import HttpResponse , HttpRequest


def home(request):
    return HttpResponse(
        "Hello World, This is my new HOME for Car Rentals Website ! "
        "we're excited to welcome you here."
    )


def about(request):
    return HttpResponse(
        "Car Rentals is a simple website that helps you find and rent "
        "the right car for your trip, whether it's a short ride or a long journey."
    )


def generate_password(request):
    length = 10
    symbols = "!@#$%^&*()-_=+?"
    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + symbols

    # نضمن وجود حرف صغير وكبير ورقم ورمز على الأقل
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(symbols),
    ]
    # نكمل بقية الطول بشكل عشوائي
    password += [secrets.choice(all_chars) for _ in range(length - len(password))]

    # نخلط الترتيب حتى ما تكون الأنواع دائماً في أول الباسورد
    secrets.SystemRandom().shuffle(password)

    return HttpResponse("".join(password))