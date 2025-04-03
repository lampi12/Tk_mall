from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(response):
	return render(response, "Tk_mall/base2.html", {})

def contact(response):
	return render(response, "Tk_mall/contact.html", {})

def about(response):
	return render(response, "Tk_mall/about.html", {})

def home(response):
	return render(response, "Tk_mall/home.html", {})

