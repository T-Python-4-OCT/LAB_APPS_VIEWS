from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("", views.page_View, name="page_View"),
    path("about/", views.about_page, name="about_page"),
    path("password/g1/", views.generate_password, name="generate_password"),
]

