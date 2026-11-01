from django.http import HttpResponse, HttpRequest
import random
import string


def FirstPage(request:HttpRequest):
    FirstPageMessage = "Hello World, This is my new HOME for Car Rentals Website ! we are excited to welcome you here."
    return HttpResponse(FirstPageMessage)


def AboutPage(request:HttpRequest):
    AboutPageMessage = ""
    return HttpResponse(" ! 🚗🔥 سيارتك علينا، والمشوار عليك")


def GeneratePasswordPage(request:HttpRequest):
    Characters = string.ascii_letters + string.digits + string.punctuation
    Password = ''.join(random.SystemRandom().choice(Characters) for _ in range(10))
    return HttpResponse(Password)