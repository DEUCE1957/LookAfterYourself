# -*- coding: utf-8 -*-
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'LookAfterYourself.settings')

import django

django.setup()
from MainApp.models import Tip,Service


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

    Services = [
        {
        "name": "Counselling and Psychological Services",
        "acronym":"CAPS",
        "description":"A UofG service that provides drop-in sessions, counselling and self-help. Located at 67 Southpark Avenue, they are open from 09:00-20:00 on Tuesday and Thurday and 09:00-17:00 on other weekdays.",
        "phone_number":"+44 (0) 141 330 4528",
        "email":"studentcounselling@glasgow.ac.uk",
        "url":"https://www.gla.ac.uk/myglasgow/counselling/",
        },
        {
        "name": "The Samaritans Glasgow",
        "acronym":"The Samaritans",
        "description":"A safe, confidential call-line to discuss anything on your mind. Available 24/7 without waiting lists and without costs. Also available at 210 West George Street for drop-ins from 09:00-20:00",
        "phone_number":"116 123",
        "email":"jo@samaritans.org",
        "url":"https://www.samaritans.org/branches/samaritans-glasgow",
        },
        {
        "name": "Breathing Space",
        "acronym":"Breathing Space",
        "description":"Sometimes our thoughts and feelings can overwhelm us. It helps to get some Breathing Space. Pick up the phone - we're here to listen.",
        "phone_number":"0800 83 85 87",
        "email":"info@breathingspacescotland.co.uk",
        "url":"http://breathingspace.scot/",
        },
        {
        "name": "National Health Service 24",
        "acronym":"NHS 24",
        "description":"Out-of-hour health advice for emergency situations",
        "phone_number":"111",
        "email":"patientaffairs@nhs24.scot.nhs.uk",
        "url":"https://www.nhs24.scot/",
        },
        {
        "name": "University of Glasgow's Nightline",
        "acronym":"GU Nightline",
        "description":"Nightline is a confidential telephone support and information service run for students, by trained student volunteers. We are available Monday to Friday from 7pm till 7am and we offer confidential listening and information to all students from Glasgow University.",
        "phone_number":"0141 334 9516",
        "email":"asknightline@glasgowstudent.net",
        "url":"https://www.gunightline.org/",
        },
        {
        "name": "B-eat beating eating disorders",
        "acronym":"B-eat",
        "description":"We are a champion, guide and friend to anyone affected by eating disorders, giving individuals experiencing an eating disorder and their loved ones a place where they feel listened to, supported and empowered.",
        "phone_number":"8088010811",
        "email":"info@beateatingdisorders.org.uk",
        "url":"https://www.beateatingdisorders.org.uk/",
        },
        {
        "name": "No Panic",
        "acronym":"NP",
        "description":"No Panic is a registered charity which helps people who suffer from Panic Attacks, Phobias, Obsessive Compulsive Disorders and other related anxiety disorders.",
        "phone_number":"8449674848",
        "email":"admin@nopanic.org.uk",
        "url":"https://www.nopanic.org.uk/",
        },
    ]


    servicesDict = {"services":Services}
    tipsDict = {"tips": tips}

    for s,s_data in servicesDict.items():
        for s in s_data:
            add_service(s["name"],s["acronym"],s["description"],s["phone_number"],s["email"],s["url"])

    for s in Service.objects.all():
        print("- {0}".format(str(s)))

    for t, tip_data in tipsDict.items():
        for x in tip_data:
            add_tip(x["title"], x["tip"], x["tags"])

    for x in Tip.objects.all():
        print("- {0}".format(str(x)))

def add_service(name,acronym,description,phone_number,email,url):
    s = Service.objects.get_or_create(name=name,acronym=acronym,description=description,phone_number=phone_number,email=email,url=url)[0]
    s.save()
    return s

def add_tip(title, tip, tags):
    x = Tip.objects.get_or_create(title=title, tip=tip, tags=tags)[0]
    x.save()
    return x


if __name__ == '__main__':
    print("Starting Population Script...")
    populate()
