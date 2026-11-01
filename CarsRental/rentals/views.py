import secrets
import string

from django.http import HttpResponse
from django.views.decorators.cache import never_cache


def home(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.", content_type="text/plain")


def about(request):
    return HttpResponse("A simple paragraph about Car Rentals. ", content_type="text/plain")


@never_cache
def generate_password(request):
    groups = (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation)
    characters = [secrets.choice(group) for group in groups]
    alphabet = "".join(groups)
    characters.extend(secrets.choice(alphabet) for _ in range(6))
    secrets.SystemRandom().shuffle(characters)
    return HttpResponse("".join(characters), content_type="text/plain")
