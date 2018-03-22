from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from MainApp.forms import UserForm, UserProfileForm, SubmitTipForm

import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

import MainApp.calendarlogic as calendarlogic
from MainApp.forms import eventForm


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
            message = calendarlogic.createEvent(data["name"], data["startDate"], data["startTime"],
                                      data["endDate"], data["endTime"], data.get("description"), data["location"])
        else:
            message = str(form.errors)
        contextDict["message"] = message
    contextDict["form"] = eventForm()
    return render(request,'MainApp/calendar.html', contextDict)

def event(request, eventID):
    return render(request,'MainApp/event.html', context=calendarlogic.eventContext(eventID))

def register(request):
    #Registration successful?
    registered = False
    if request.method == 'POST':

        #Retrieve info from form
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Store form data in database
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                #Save UserProfile
                profile.save()
               #Registration successful
                registered = True

            else:
                #Invalid forms
                print(user_form.errors, profile_form.errors)

    else:
        #Render forms
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
                    'MainApp/register.html',
                    {'user_form': user_form,
                    'profile_form': profile_form,
                    'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Checks if valid user
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                # If active and valid login user in
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # Cannot log in if inactive
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # Not POST so display login form
    else:
        return render(request, 'MainApp/login.html', {})

#Purely for diagnosis
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('index'))


def submit_tip(request):
    form = SubmitTipForm()

    # Check that the request was POST
    if request.method == 'POST':
        form = SubmitTipForm(request.POST)

        # Check that the submitted form was valid
        if form.is_valid():
            # Save to the database if true
            form.save(commit=True)
            # Return the user to the index page if form was successfully submitted
            return index(request)
        else:
            # Print the errors to the console
            print(form.errors)
    # Handle bad/new/no form cases and render any error messages
    return render(request, 'MainApp/submittip.html', {'form': form})