from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post


# class view
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


# function view
def about(request) -> HttpResponse:
    context = {
        "title": "About"
    }
    return render(request, "blog/about.html", context)
