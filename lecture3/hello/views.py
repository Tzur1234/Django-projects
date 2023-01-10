from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request, name):
    return render(request, "hello/index.html", {
        "name": name.capitalize()
    })

def greet(request):
    return render(request, "hello/index.html", {
        "name": '(Uknonw name)'
    })

def func1(request):
    return render(request, "hello/index.html")