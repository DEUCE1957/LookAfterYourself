from django.test import TestCase

from django.core.urlresolvers import reverse

from django.contrib.admin.views.decorators import staff_member_required

import datetime
# Create your tests here.

###Tests for the calendar###

class CalendarViewTests(TestCase):
    def test_id_doesnt_exist(self):
        response = self.client.get(reverse('event', args=['doesntexist']))
        self.assertContains(response, "The event doesn&#39;t exist.")

    def test_next_event_is_in_the_future(self):
        response = self.client.get(reverse('calendar'))
        stringStart = response.context["startTime"]
        if len(stringStart) > 29:
            start = datetime.datetime.strptime(stringStart,"%a, %d %B, %H:%M, %Y")
        else:
            start = datetime.datetime.strptime(stringStart,"%a, %d %B, %H:%M")
            start = start.replace(year = datetime.datetime.now().year)
        self.assertTrue(start > datetime.datetime.now())

    @staff_member_required
    def staff_users_see_form(request):
        response = self.client.get(reverse('calendar'))
        self.assertContains(response, "Create a new event")

    def normal_users_dont_see_form(request):
        response = self.client.get(reverse('calendar'))
        self.assertNotContains(response, "Create a new event")
    
