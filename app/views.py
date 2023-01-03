from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses-page.html')

def contact(request):
    return render(request, 'contact.html')