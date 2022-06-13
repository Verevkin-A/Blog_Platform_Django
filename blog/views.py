from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Verevkin",
        "title": "First post",
        "content": "First post content",
        "date_posted": "June 13, 2022"
    },
    {
        "author": "Alex",
        "title": "Second post",
        "content": "Some interesting content",
        "date_posted": "June 13, 2022"
    }
]


def home(request) -> HttpResponse:
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)


def about(request) -> HttpResponse:
    return render(request, "blog/about.html", {"title": "About"})
