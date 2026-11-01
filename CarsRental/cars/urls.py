from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("about/", views.about, name="about"),
    path("password/generate/", views.randomly_generated_password, name="randomly_generated_password"),
]