from django.contrib import admin
from .models import Post

# show posts table for superusers
admin.site.register(Post)
