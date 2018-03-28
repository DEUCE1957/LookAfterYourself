from django.test import TestCase

from django.core.urlresolvers import reverse

from django.contrib.admin.views.decorators import staff_member_required

from MainApp.models import Tip

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



### Tests for Tips ###

class TipModelTests(TestCase):
    def test_ensure_ids_are_integers(self):
        # Create test objects where one should return true and one should return false
        test1 = Tip(tipId=1, title='test title', tip='test tip', tags='general')
        test2 = Tip(tipId='2', title='abc', tip='123', tags='general')

        test1.save()
        test2.save()

        self.assertEqual((test1.tipId == 1), True)
        self.assertEqual((test2.tipId == 2), False)


    def test_ensure_titles_are_max_128_chars(self):
        # Create test objects where one should return true and one should return false
        test3 = Tip(tipId=1, title='test title', tip='test tip 3', tags='general')
        test4 = Tip(tipId=2, title='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et ma', tip='test tip 4', tags='general')

        test3.save()
        test4.save()

        self.assertTrue(len(test3.title) <= 128)
        self.assertFalse(len(test4.title) <= 128)


    def test_ensure_tips_are_max_1000_chars(self):
        # Create test objects where one should return true and one should return false
        test5 = Tip(tipId=1, title='test title', tip='test tip 5', tags='general')
        test6 = Tip(tipId=2, title='test title 2', tip=('x' * 1001), tags='general')

        test5.save()
        test6.save()

        self.assertTrue(len(test5.tip) <= 1000)
        self.assertFalse(len(test6.tip) <= 1000)