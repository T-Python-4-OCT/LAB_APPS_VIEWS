from django.shortcuts import render
import random
import string
from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    )


def about(request):
    return HttpResponse("نوفّر لك السيارة المناسبة بأسعار منافسة وخدمة موثوقة، لتنطلق في رحلتك بكل راحة وثقة.")


def generate_password(request):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(10))
    return HttpResponse(password)
