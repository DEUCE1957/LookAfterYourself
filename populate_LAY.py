# -*- coding: utf-8 -*-
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'LookAfterYourself.settings')

import django

django.setup()
from MainApp.models import Tip


def populate():
    tips = [
        {"title": "Know your limitations, but focus on your strong points",
         "tip": "You probably can’t handle as much stress as other people."
                "So maybe you don’t get as much done in a day. But the flip side of that "
                "is that you’re probably a pretty patient human being.That’s going to make a lot "
                "of people want to be your friend. I’m not sure why, but it seems like people with "
                "mental illnesses are overrepresented in the brains and creativity department. "
                "Autism often comes with great attention to detail and the same type of associative "
                "thinking as schizophrenia. And we all know how many artists are bipolar.",
         "tags": "anxiety"},
        {"title": "Staying Hydrated",
         "tip": "It's recommended that you drink between 6-8 glasses of fluid per day. Water is a cheap "
                "and healthy option",
         "tags": "depression anxiety"}]

    tipsDict = {"tips": tips}

    for t, tip_data in tipsDict.items():
        for x in tip_data:
            add_tip(x["title"], x["tip"], x["tags"])

    for x in Tip.objects.all():
        print("- {0}".format(str(x)))


def add_tip(title, tip, tags):
    x = Tip.objects.get_or_create(title=title, tip=tip, tags=tags)[0]
    x.save()
    return x


if __name__ == '__main__':
    print("Starting Population Script...")
    populate()
