from django.http import HttpRequest,HttpResponse
import random
import string



def home(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here.")


def about(request):
    return HttpResponse("A simple paragraph about Car Rentals.")


def password_generator(request):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(10))

    return HttpResponse(password)
