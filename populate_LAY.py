# -*- coding: utf-8 -*-
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'LookAfterYourself.settings')

import django

django.setup()
from MainApp.models import Tip,Service, Post


def populate():
    tips = [
        {"title": "Learn how to calm your anxiety by relaxing the muscles in your body",
          "tip": "Calm breathing and progressive muscle relaxation can you help to reduce some "
          "of the anxious and tense feelings in your body.",
          "tags": "ptsd anxiety general"},

        {"title": "Know your limitations, but focus on your strong points",
         "tip": "You probably can’t handle as much stress as other people."
                "So maybe you don’t get as much done in a day. But the flip side of that "
                "is that you’re probably a pretty patient human being.That’s going to make a lot "
                "of people want to be your friend. I’m not sure why, but it seems like people with "
                "mental illnesses are overrepresented in the brains and creativity department. "
                "Autism often comes with great attention to detail and the same type of associative "
                "thinking as schizophrenia. And we all know how many artists are bipolar.",
         "tags": "anxiety"},

        {"title": "Create Space",
          "tip": "Ask yourself what you need on a daily basis, and find storage bins or closets for "
          "things you don’t. Designate specific areas for things like keys, bills, and other items "
          "that can be easily misplaced. Throw away things you don’t need.",
          "tags": "adhd"},

         {"title": "Take a Shower",
          "tip": "not a bath, a shower. use water as hot or cold as u like. u dont even need to wash."
                " just get in under the water and let it run over you for a while. sit on the "
                "floor if you gotta.",
          "tags": "general depression"},

        {"title": "Addiction =/= Bad/Weak",
          "tip": "If you fall back into old patterns (backslide) a bit, talk to someone as soon as "
          "possible. There's nothing to be ashamed about, but it's important to get help soon so that "
          "all of the hard work you put into your recovery is not lost.",
          "tags": "addiction"},

        {"title": "Staying Hydrated",
         "tip": "It's recommended that you drink between 6-8 glasses of fluid per day. Water is a cheap "
                "and healthy option",
         "tags": "depression anxiety general"},

        {"title": "Relax Before You Go To Bed",
         "tip": "Do something calming. Breathing exercises. Muscle relaxation. Meditation.",
         "tags": "general"},

         {"title": "Use a calendar app or day planner",
          "tip": "Effective use of a day planner or a calendar on your smartphone or computer can help you "
          "remember appointments and deadlines. With electronic calendars, you can also set up automatic reminders "
          "so scheduled events don’t slip your mind.",
          "tags": "adhd"},

        {"title": "Moisturise Everything",
          "tip": "Use whatever lotion u like. unscented? dollar store lotion? fancy 48 hour lotion that makes u"
          "smell like a field of wildflowers? use whatever u want, and use it all over.",
          "tags": "depression"},

        {"title": "Figure Out Who Will Accept You",
         "tip": "A lot of us are charismatic in small doses. That gives people high expectations. But when we "
                "can’t be “on” consistently enough to meet those expectations it feels like we’re letting people down. "
                "There are some people you can be around all the time and others who are only able to deal with you "
                "on good days. That’s okay. Every friendship has a different purpose. Sometimes you fit with someone "
                "so well in some ways that it makes up for all the others.",
         "tags": "ptsd ocd anxiety bipolar"},

         {"title": "Change",
          "tip": "Put on some clean and comfortable clothes. It will make you feel better than you imagine.",
          "tags": "general"},

        {"title": "Use Lists",
          "tip": "Make use of lists and notes to keep track of regularly scheduled tasks, projects, deadlines, and "
          "appointments. If you decide to use a daily planner, keep all lists and notes inside it. You also have many "
          "options for use on your smartphone or computer. Search for “to do” apps or task managers.",
          "tags": "adhd general"},

        {"title": "Avoid High-Risk Situations",
          "tip": "Some common high-risk situations are described by the acronym, HALT: (H)ungy (A)ngry (L)onely (T)ired.",
          "tags": "addiction"},

        {"title": "Don't Let People Treat You Badly",
         "tip": "A lot of us are easy prey for abusive partners and “friends” who want to make everyone around them as "
                "miserable as they are. I dated a controlling guy in high school who subtly tried to change my opinion "
                "of my family. I was vaguely aware that he wasn’t a good person, but I was so flattered by the "
                "attention that I put up with it until my parents wouldn’t let me see him anymore.",
         "tags": "general"},

         {"title": "Clean Something",
          "tip": "doesn’t have to be anything big. organize one drawer of ur desk. wash five dirty dishes. do a load of "
          "laundry. scrub the bathroom sink. ",
          "tags": "general depression ocd"},

        {"title": "Grounding",
          "tip": "Grounding is a very helpful technique if you are experiencing flashbacks and you find yourself sometimes "
          "losing touch with the present moment. Having this symptom of PTSD is not only terrifying for you, but it can also "
          "be scary for people around you, such as friends and family. Grounding teaches you to stop losing touch with the "
          "present moment by concentrating and focusing on the present or by directing your attention to something else.",
          "tags": "ptsd"},

        {"title": "Be Honest",
          "tip": "An addiction requires lying. You have to lie about getting your drug, using it, hiding its consequences,"
          " and planning your next relapse. An addiction is full of lying. By the time you've developed an addiction, "
          "lying comes easily to you. After a while you get so good at lying that you end up lying to yourself. That's "
          "why addicts don't know who they are or what they believe in.",
          "tags": "addiction"},

        {"title": "Deal With It Now",
          "tip": "You can avoid forgetfulness, clutter, and procrastination by filing papers, cleaning up messes, or "
          "returning phone calls immediately, not sometime in the future. If a task can be done in two minutes or less, "
          "do it on the spot, rather than putting it off for later.",
          "tags": "adhd"},

        {"title": "Get Treatment",
         "tip": "Please. Two of my friends committed suicide because they hadn’t dealt with their illnesses properly. "
                "You might be ashamed, but there’s way more shame in hurting people who need you because you don’t "
                "want to admit that you have a problem.",
         "tags": "addiction depression eatingdisorder"},

        {"title": "Blast Music",
          "tip": " listen to something upbeat and dancey and loud, something that’s got lots of energy. sing to "
          "it, dance to it, even if you suck at both.",
          "tags": "general depression bipolar"},

        {"title": "Break Tasks Down Into Smaller Steps",
         "tip": "A common symptom of depression is the feeling of being overwhelmed even by ordinary day-to-day tasks. "
                "Even getting out of bed and getting dressed can feel like a huge hurdle and people become more "
                "withdrawn and less active as depression becomes more severe. The best way to overcome feeling "
                "overwhelmed is to break down the activity in small, easier-to-achieve chunks.",
         "tags": "anxiety depression ocd"},

        {"title": "Make Yourself Some Food",
          "tip": "don’t just grab a granola bar to munch. take the time and make food. even if it’s ramen. "
          "add something special to it, like a hard boiled egg or some veggies. prepare food, it tastes way "
          "better, and you’ll feel like you accomplished something.",
          "tags": "general depression eatingdisorder"},

        {"title": "Avoid Isolation By Connecting With People",
         "tip": "People with depression often cut themselves off from the outside world. But becoming withdrawn and "
                "less talkative can create a downward spiral. Connection is one of the six basic emotional needs "
                "and when depression takes hold it is often the need that gets most neglected in favour of satisfying "
                "the need for comfort through isolation.",
         "tags": "depression general"},

        {"title": "Make Something",
          "tip": "write a short story or a poem, draw a picture, color a picture, fold origami, crochet or knit, "
          "sculpt something out of clay, anything artistic. even if you don’t think you’re good at it.",
          "tags": "general depression ocd anxiety"},

        {"title": "Accept Personal Responsibility",
         "tip": "The power of the mind is an amazing thing, and although pharmaceutical intervention is certainly "
                "beneficial in cases of severe depression, individuals can work towards overcoming mild or moderate "
                "depression faster if they start to take personal responsibility for their actions and behaviours. "
                "This advice is not about “pulling yourself together” but more about what decisions need to be made "
                "by the individual to make them feel more powerful and happy.",
         "tags": "depression"},

        {"title": "Go Outside",
          "tip": "take a walk. sit in the grass. look at the clouds. smell flowers. put your hands in the dirt "
          "and feel the soil against your skin.",
          "tags": "depression"},

        {"title": "Call Someone",
          "tip": "call a loved one, a friend, a family member, call a chat service if you have no one else to call. "
          "talk to a stranger on the street. have a conversation and listen to someone’s voice. if you can’t, text "
          "or email or whatever, just have some social interaction with another person. even if you don’t say "
          "much, listen to them.",
          "tags": "general depression anxiety bipolar"},

        {"title": "Have Regular Sleep Time",
         "tip": "Getting a good night’s sleep is important for everyone but especially for those suffering from "
                "depression. Conversely too much sleep (over eight hours) can exacerbate depression. Regular "
                "sleeping hours are essential in managing mood and having a regular bedtime and rise time is "
                "important. Go back to basics, set alarms, create a routine and introduce calming rituals before bed.",
         "tags": "general"},

        {"title": "Have Pets?",
          "tip": "cuddle your pets if you have them/can cuddle them. take pictures of them. talk to them. tell them "
          "how u feel, about your favorite movie, a new game coming out. anything you are excited about for the future.",
          "tags": "general depression anxiety bipolar"}]

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
    Posts = [
        {
            "title" : "Test Post",
            "content":  "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis " \
                       "parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo," \
                       " fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium." \
                       " Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, " \
                       "enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam " \
                       "ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper " \
                       "libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. " \
                       "Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. " \
                       "Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. " \
                       "Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum " \
                       "ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu " \
                       "tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed aliquam ultrices mauris. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, " \
                       "mauris. Praesent adipiscing. Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. Vestibulum volutpat pretium libero. Cras id dui. Aenean ut eros et " \
                       "nisl sagittis vestibulum. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede. Sed lectus. Donec mollis hendrerit risus. Phasellus nec " \
                       "sem in justo pellentesque facilisis. Etiam imperdiet imperdiet orci. Nunc nec neque. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi. Curabitur " \
                       "ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Maecenas malesuada. Praesent congue erat at massa. Sed cursus turpis vitae tortor. Donec " \
                       "posuere vulputate arcu. Phasellus accumsan cursus velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed aliquam, " \
                       "nisi quis porttitor congue, elit erat euismod orci, ac placerat dolor lectus quis orci. Phasellus consectetuer vestibulum elit. Aenean tellus metus, bibendum " \
                       "sed, posuere ac, mattis non, nunc. Vestibulum fringilla pede sit amet augue. In turpis. Pellentesque posuere. ",
        },
        {
            "title": "Test Post # 1",
            "content":  "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis " \
                       "parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo," \
                       " fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium." \
                       " Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, " \
                       "enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam " \
                       "ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper " \
                       "libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. " \
                       "Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. " \
                       "Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. " \
                       "Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum " \
                       "ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu " \
                       "tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed aliquam ultrices mauris. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, " \
                       "mauris. Praesent adipiscing. Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. Vestibulum volutpat pretium libero. Cras id dui. Aenean ut eros et " \
                       "nisl sagittis vestibulum. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede. Sed lectus. Donec mollis hendrerit risus. Phasellus nec " \
                       "sem in justo pellentesque facilisis. Etiam imperdiet imperdiet orci. Nunc nec neque. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi. Curabitur " \
                       "ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Maecenas malesuada. Praesent congue erat at massa. Sed cursus turpis vitae tortor. Donec " \
                       "posuere vulputate arcu. Phasellus accumsan cursus velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed aliquam, " \
                       "nisi quis porttitor congue, elit erat euismod orci, ac placerat dolor lectus quis orci. Phasellus consectetuer vestibulum elit. Aenean tellus metus, bibendum " \
                       "sed, posuere ac, mattis non, nunc. Vestibulum fringilla pede sit amet augue. In turpis. Pellentesque posuere. ",
        },

    ]



    servicesDict = {"services":Services}
    tipsDict = {"tips": tips}
    postsDict = {"posts": Posts}

    for p, p_data in postsDict.items():
        for p in p_data:
            add_post(p["title"], p["content"])

    for p in Service.objects.all():
        print("- {0}".format(str(p)))

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

def add_post(title, content):
    p = Post.objects.get_or_create(title=title, content=content)[0]
    p.save()
    return p

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

