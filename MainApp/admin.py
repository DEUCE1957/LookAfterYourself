from django.contrib import admin

# Register your models here.

from MainApp.models import Tip
from MainApp.models import UserProfile

admin.site.register(Tip)
admin.site.register(UserProfile)