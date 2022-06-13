from django.shortcuts import render
from django.http import HttpResponse


def home(request) -> HttpResponse:
    return render(request, "blog/home.html")


def about(request) -> HttpResponse:
    return render(request, "blog/about.html")
