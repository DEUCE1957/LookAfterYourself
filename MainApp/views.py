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

##Copy pasted from Google's quickStart
def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

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
    contextDict = {}
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the event')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=1, singleEvents=True,
        orderBy='startTime').execute()
    event = eventsResult.get('items', [])[0]
    contextDict["name"] = event["summary"]
    contextDict["time"] = event["start"]["dateTime"]
    contextDict["description"] = event.get("description","")
    contextDict["color"] = event.get("colorId", "#ffffff")
    contextDict["id"] = event["id"]
    return render(request,'MainApp/calendar.html', context=contextDict)

def event(request, eventID):
    contextDict = {}
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the event')
    event = service.events().get(calendarId="primary",eventId=eventID).execute()
    
    contextDict["name"] = event["summary"]
    contextDict["time"] = event["start"]["dateTime"]
    contextDict["description"] = event.get("description","")
    contextDict["color"] = event.get("colorId", "#ffffff")

    return render(request,'MainApp/event.html', context=contextDict)

def login(request):
    return HttpResponse("This is the Look After Yourself login page")

# Create your views here.
