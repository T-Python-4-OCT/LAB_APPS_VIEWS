from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string


def page_View(request: HttpRequest):
    cor1 = "Hello World, This is my new HOME for Car" \
    " Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(cor1)


def about_page(request: HttpRequest):
    cor = "We're not the only ones, but we're the best"
    return HttpResponse(cor)


def generate_password(request: HttpRequest):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))
    return HttpResponse(password)