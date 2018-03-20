from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

##Copy pasted from Google's quickStart
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'
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

#Creates a recourse for calendar
def service():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    return service

def getDateTime(time):
    return datetime.datetime.strptime(time,"%Y-%m-%dT%H:%M:%SZ")

def createTestEvent(ser):
    event = {
  'summary': 'Google I/O 2015',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%dT%H:%M:%S"),
    'timeZone': 'Etc/GMT+0',
  },
  'end': {
    'dateTime': datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(hours=1), "%Y-%m-%dT%H:%M:%S"),
    'timeZone': 'Etc/GMT+0',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [],
  'reminders': {},}
    event = ser.events().insert(calendarId='primary', body=event).execute()
    print(event)

def createEvent(name, startDate, startTime, endDate, endTime, description=""):
    ser = service()
    event = {
  'summary': name,
  'description': description,
  'start': {
    'dateTime': datetime.datetime.strftime(datetime.datetime.combine(startDate,startTime),
                                           "%Y-%m-%dT%H:%M:%S"),
    'timeZone': 'Etc/GMT+0',
  },
  'end': {
    'dateTime': datetime.datetime.strftime(datetime.datetime.combine(endDate,endTime),
                                           "%Y-%m-%dT%H:%M:%S"),
    'timeZone': 'Etc/GMT+0',
  },
  'recurrence': [],
  'attendees': [],
  'reminders': {},}
    event = ser.events().insert(calendarId='primary', body=event).execute()
    print(event)

def context(event):
    contextDict = {}
    now = datetime.datetime.now()
    contextDict["name"] = event["summary"]
    startTime = getDateTime(event["start"]["dateTime"])
    #If the year is different from the current year, we add it
    if startTime.year != now.year:
        contextDict["startTime"] = datetime.datetime.strftime(startTime,"%a, %d %B, %H:%M, %Y")
    else:
        contextDict["startTime"] = datetime.datetime.strftime(startTime,"%a, %d %B, %H:%M")
    endTime = getDateTime(event["end"]["dateTime"])
    #If the end date is different, we'll add it, otherwise we'll have just the time
    if startTime.year != endTime.year:
        contextDict["endTime"] = datetime.datetime.strftime(endTime,"%a, %d %B, %H:%M, %Y")
    elif startTime.day != endTime.day or startTime.month != endTime.month:
        contextDict["endTime"] = datetime.datetime.strftime(endTime,"%a, %d %B, %H:%M")
    else:
        contextDict["endTime"] = datetime.datetime.strftime(endTime,"%H:%M")
    contextDict["description"] = event.get("description","")
    contextDict["color"] = event.get("colorId", "#ffffff")
    contextDict["id"] = event["id"]
    return contextDict

def getPrevEventId(ser,event):
    timeMax = event["start"]["dateTime"]
    eventsResult = ser.events().list(
        calendarId='primary', timeMax=timeMax, singleEvents=True,
        orderBy='startTime').execute()
    if len(eventsResult.get('items', [])) < 1:
        return ""
    else:
        return eventsResult.get('items', [])[-1]["id"]

def getNextEventId(ser, event):
    timeMin = event["start"]["dateTime"]
    eventsResult = ser.events().list(
        calendarId='primary', timeMin=timeMin, maxResults=2, singleEvents=True,
        orderBy='startTime').execute()
    if len(eventsResult.get('items', [])) < 2:
        return ""
    else:
        return eventsResult.get('items', [])[1]["id"]

def calendarContext():
    ser = service()
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the event')
    eventsResult = ser.events().list(
        calendarId='primary', timeMin=now, maxResults=1, singleEvents=True,
        orderBy='startTime').execute()
    event = eventsResult.get('items', [])[0]
    return context(event)

def eventContext(eventID):
    ser = service()
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the event')
    event = ser.events().get(calendarId="primary",eventId=eventID).execute()
    contextDict = context(event)
    idholder = getNextEventId(ser, event)
    if idholder != "":
        contextDict["next"] = idholder
    idholder = getPrevEventId(ser, event)
    if idholder != "":
        contextDict["prev"] = idholder
    return contextDict

if __name__ == '__main__':
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None
    createEvent("AA", 2018,4,4,12,0,2018,4,5,3,3,"Let us see if this works")
    print("created event")
