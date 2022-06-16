from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post


# class-based view
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


class PostDetailView(DetailView):
    model = Post


# function view
def about(request) -> HttpResponse:
    context = {
        "title": "About"
    }
    return render(request, "blog/about.html", context)
