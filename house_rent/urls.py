# house_rent/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views  # Import the home view

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('admin/', admin.site.urls),
    path('api/', include('properties.urls')),  # API routes
]
