from django.shortcuts import render
from .models import *


def home(requests):
    return render(requests, "home.html")


def about(requests):
    return render(requests, "about.html")


def blog(requests):
    content = {
        "maqolalar": Maqola.objects.all()
    }
    return render(requests, "blog.html", content)


def maqola(requests, slug):
    content = {
        "maqola": Maqola.objects.filter(slug=slug)
    }
    return render(requests, "maqola.html",content)
