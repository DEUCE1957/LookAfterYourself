<<<<<<< HEAD
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

class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    # Additional Attributes
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username


=======
from __future__ import unicode_literals

from django.db import models
from django import forms
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify
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
    # Additional Attributes
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username

class BlogEntry(models.Model):
    #An instance for a blog post
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=10000)
    tags = models.CharField(max_length=1000)
    time = models.DateTimeField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Blog entries'
>>>>>>> 2e6026cdfe1357ee2587c1d0aeb8f7300ad9f20a
