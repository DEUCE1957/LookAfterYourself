from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'custom_message':"This is a customised message"}
    return render(request,'MainApp/index.html', context=context_dict)

def blog(request):
    return render(request,'MainApp/blog.html', context={})

def tips(request):
    return HttpResponse("This is the Look After Yourself tips page")

def support(request):
    return HttpResponse("This is the Look After Yourself support services page")

def calendar(request):
    return HttpResponse("This is the Look After Yourself calendar page")

def login(request):
    return HttpResponse("This is the Look After Yourself login page")

# Create your views here.
