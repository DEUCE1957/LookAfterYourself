from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the Look After Yourself index page")

def blog(request):
    return HttpResponse("This is the Look After Yourself blog page")

def tips(request):
    return HttpResponse("This is the Look After Yourself tips page")

# Create your views here.
