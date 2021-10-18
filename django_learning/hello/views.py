from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index0(request):
    return HttpResponse("Hello, world!")

def index1(request):
    return render(request, "hello/index.html")

def fei(request):
    return HttpResponse("Hello, Fei!")

def greet0(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")

def greet1(request, name):
    return render(request, "hello/greet.html", {
        "name" : name.capitalize()
        })
