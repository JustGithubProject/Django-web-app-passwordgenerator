from django.shortcuts import render
import random
import datetime


def home(request):
    return render(request, "home.html")


def about(request):
    y = datetime.datetime.now().year
    return render(request, "about.html", {'year': y})


def password(request):
    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    numbers = request.GET.get('numbers')
    symbols = request.GET.get("symbols")

    chars = list('')
    if uppercase:
        chars.extend("QWERTYUIOPASDFGHJKLZXCVBNM")
    if numbers:
        chars.extend("1234567890")
    if symbols:
        chars.extend("@#$%&")

    thepass = ''
    for i in range(length):
        thepass += random.choice(chars)
    return render(request, "password.html", {'password': thepass})