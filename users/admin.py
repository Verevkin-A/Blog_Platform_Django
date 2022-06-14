from django.contrib import admin
from .models import Profile

# show profiles table for superusers
admin.site.register(Profile)
