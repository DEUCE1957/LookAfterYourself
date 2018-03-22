from __future__ import unicode_literals

from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class Tip(models.Model):
    tipId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    tip = models.CharField(max_length=1000)
    tags = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.tipId)


class SubmittedTip(models.Model):
    tipId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    tip = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.tipId)


class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    # Additional Attributes
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username

class Service(models.Model):
    #Full Name of Service
    name = models.CharField(max_length=128, unique=True)
    #Acronym
    acronym = models.CharField(max_length=10)
    #Link to the Service's WebPage
    url = models.URLField(max_length=200)
    #description
    desc = models.CharField(max_length=450)
    #phone number
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    class Meta:
        verbose_name_plural = 'Services'

    def __str__(self):
        return str(self.ServiceID)

