from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("<h1>About</h1>")

def contact(request):
    return render(request, 'contact.html')

def detail(request):
    return HttpResponse("<h1>Details</h1>")

def thanks(request):
    return HttpResponse("<h1>Thank you</h1>")
