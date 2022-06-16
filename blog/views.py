from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post


# class-based view
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


class PostDetailView(DetailView):
    """View existing post view"""
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """Create new post view"""
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update existing post view"""
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Testing if updated post is owned by user"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# function view
def about(request) -> HttpResponse:
    context = {
        "title": "About"
    }
    return render(request, "blog/about.html", context)
