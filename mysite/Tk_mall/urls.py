from django.urls import path

from . import views

urlpatterns = [
path("", views.index, name="index"),
path("contact-us/", views.contact, name="Contact Us"),
path("about/", views.about, name="About Us"),
path("home/", views.home, name="Home Page"),
]
	
