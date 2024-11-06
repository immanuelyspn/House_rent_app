# house_rent/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the House Rent App API")
