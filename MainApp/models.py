
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tip(models.Model):
    tipId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    tip = models.CharField(max_length=1000)
    tags = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.tipId)


class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username


# Create model for table in the database to store user submitted suggestions
class Suggestion(models.Model):
    # Have the primary key as an auto-incrementing field to avoid clashes
    suggestionId = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=128)
    suggestion = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.suggestionId)


class Service(models.Model):
    serviceId=models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    acronym = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to='service_images',blank=True)

    last_updated = models.DateField(auto_now=True)
    #Contact Information
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    url = models.URLField(max_length=200)

    def __str__(self):
        return str(self.serviceId)


class Submission(models.Model):
    tipId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    tip = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.tipId)


class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Date of publication')
    content = models.TextField(max_length=10000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

