# -*- coding: utf-8 -*-
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'LookAfterYourself.settings')

import django

django.setup()
from MainApp.models import Tip
from MainApp.models import Service

#IDcount = 0

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
         "tags": "depression anxiety general"},

        {"title": "Relax Before You Go To Bed",
         "tip": "Do something calming. Breathing exercises. Muscle relaxation. Meditation.",
         "tags": "general"},

        {"title": "Figure Out Who Will Accept You",
         "tip": "A lot of us are charismatic in small doses. That gives people high expectations. But when we "
                "can’t be “on” consistently enough to meet those expectations it feels like we’re letting people down. "
                "There are some people you can be around all the time and others who are only able to deal with you "
                "on good days. That’s okay. Every friendship has a different purpose. Sometimes you fit with someone "
                "so well in some ways that it makes up for all the others.",
         "tags": "ptsd ocd anxiety bipolar"},

        {"title": "Don't Let People Treat You Badly",
         "tip": "A lot of us are easy prey for abusive partners and “friends” who want to make everyone around them as "
                "miserable as they are. I dated a controlling guy in high school who subtly tried to change my opinion "
                "of my family. I was vaguely aware that he wasn’t a good person, but I was so flattered by the "
                "attention that I put up with it until my parents wouldn’t let me see him anymore.",
         "tags": "general"},

        {"title": "Get Treatment",
         "tip": "Please. Two of my friends committed suicide because they hadn’t dealt with their illnesses properly. "
                "You might be ashamed, but there’s way more shame in hurting people who need you because you don’t "
                "want to admit that you have a problem.",
         "tags": "addiction depression eatingdisorder"},

        {"title": "Break Tasks Down Into Smaller Steps",
         "tip": "A common symptom of depression is the feeling of being overwhelmed even by ordinary day-to-day tasks. "
                "Even getting out of bed and getting dressed can feel like a huge hurdle and people become more "
                "withdrawn and less active as depression becomes more severe. The best way to overcome feeling "
                "overwhelmed is to break down the activity in small, easier-to-achieve chunks.",
         "tags": "anxiety depression ocd"},

        {"title": "Avoid Isolation By Connecting With People",
         "tip": "People with depression often cut themselves off from the outside world. But becoming withdrawn and "
                "less talkative can create a downward spiral. Connection is one of the six basic emotional needs "
                "and when depression takes hold it is often the need that gets most neglected in favour of satisfying "
                "the need for comfort through isolation.",
         "tags": "depression general"},

        {"title": "Accept Personal Responsibility",
         "tip": "The power of the mind is an amazing thing, and although pharmaceutical intervention is certainly "
                "beneficial in cases of severe depression, individuals can work towards overcoming mild or moderate "
                "depression faster if they start to take personal responsibility for their actions and behaviours. "
                "This advice is not about “pulling yourself together” but more about what decisions need to be made "
                "by the individual to make them feel more powerful and happy.",
         "tags": "depression"},

        {"title": "Have Regular Sleep Time",
         "tip": "Getting a good night’s sleep is important for everyone but especially for those suffering from "
                "depression. Conversely too much sleep (over eight hours) can exacerbate depression. Regular "
                "sleeping hours are essential in managing mood and having a regular bedtime and rise time is "
                "important. Go back to basics, set alarms, create a routine and introduce calming rituals before bed.",
         "tags": "general"}]

    #services = [
    #    {"name" : "Counselling and Psychological Services",
    #    "acronym" : "CAPS",
    #    "url" : "https://www.gla.ac.uk/myglasgow/counselling/",
    #    "desc" : "A UofG service that provides drop-in sessions, counselling and self-help",
    #    "phone_number" : "+4401413304528",
    #    },
    #    {"name" : "The Samaritans",
    #    "acronym" : "",
    #    "url" : "https://www.samaritans.org/branches/samaritans-glasgow",
    #    "desc" : "A safe, confidential call-line to discuss anything on your mind. Available 24/7 without waiting lists and without costs.",
    #    "phone_number" : "116123",
    #   }
    #]

    tipsDict = {"tips": tips}

    for t, tip_data in tipsDict.items():
        for x in tip_data:
            add_tip(x["title"], x["tip"], x["tags"])

    for x in Tip.objects.all():
        print("- {0}".format(str(x)))


#def add_service(name,acronym,url,desc,phone_number):
#    IDcount = IDcount + 1
#    service = Service.objects.get_or_create(ServiceId=IDcount,name=name,acronym=acronym,url=url,
#    desc=desc,phone_number=phone_number)[0]
#    service.save()


def add_tip(title, tip, tags):
    x = Tip.objects.get_or_create(title=title, tip=tip, tags=tags)[0]
    x.save()
    return x


if __name__ == '__main__':
    print("Starting Population Script...")
    populate()
