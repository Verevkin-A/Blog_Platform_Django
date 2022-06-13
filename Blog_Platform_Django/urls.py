"""Blog_Platform_Django URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include("blog.urls")),
    path('registration/', user_views.registration, name="registration"),
]
