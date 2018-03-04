from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'custom_message':"This is a customised message"}
    return render(request,'MainApp/index.html', context=context_dict)

def blog(request):
    return HttpResponse("This is the Look After Yourself blog page")

def tips(request):
    return HttpResponse("This is the Look After Yourself tips page")

def support(request):
    return HttpResponse("This is the Look After Yourself support services page")

def calendar(request):
    return HttpResponse("This is the Look After Yourself calendar page")

# Create your views here.
