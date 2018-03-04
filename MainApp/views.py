from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world and welcome to the Look After Yourself web app")
# Create your views here.
