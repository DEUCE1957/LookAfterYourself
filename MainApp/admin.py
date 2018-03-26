from django.contrib import admin

# Register your models here.

from MainApp.models import Tip, Submission
from MainApp.models import UserProfile
from MainApp.models import Service

admin.site.register(Tip)
admin.site.register(Submission)
admin.site.register(UserProfile)
admin.site.register(Service)




