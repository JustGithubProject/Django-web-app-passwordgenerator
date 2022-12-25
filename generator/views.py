from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def password(request):
    return render(request, "password.html")