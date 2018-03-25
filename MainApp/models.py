from __future__ import unicode_literals

from django.db import models
from django import forms
from django.contrib.auth.models import User

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

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username

class suggestion(models.Model):
    suggestionId=moels.AutoField(primary_key=True)
    subject = model.CharField(max_length=128)
    suggestion = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.suggestionId)
