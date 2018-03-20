from __future__ import print_function

from django.shortcuts import render
from django.http import HttpResponse

import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

import calendarlogic
from forms import eventForm


def index(request):
    context_dict = {'custom_message':"This is a customised message"}
    return render(request,'MainApp/index.html', context=context_dict)

def blog(request):
    return render(request,'MainApp/blog.html', context={})

def tips(request):
    return render(request,'MainApp/tips.html', context={})

def submittip(request):
    return render(request, 'MainApp/submittip.html', context={})

def support(request):
    return render(request,'MainApp/support.html', context={})

def calendar(request):
    contextDict = calendarlogic.calendarContext()
    if request.method == 'POST' and request.user.is_superuser:
        form = eventForm(request.POST)
        print(form)
        if form.is_valid():
            data = form.cleaned_data
            calendarlogic.createEvent(data["name"], data["startDate"], data["startTime"],
                                      data["endDate"], data["endTime"], data.get("description"))
        else:
            print(form.errors)
    contextDict["form"] = eventForm()
    return render(request,'MainApp/calendar.html', contextDict)

def event(request, eventID):
    return render(request,'MainApp/event.html', context=calendarlogic.eventContext(eventID))

def login(request):
    return HttpResponse("This is the Look After Yourself login page")

# Create your views here.
