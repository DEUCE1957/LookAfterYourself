from django.contrib import admin

# Register your models here.

from MainApp.models import Tip, SubmittedTip
from MainApp.models import UserProfile

admin.site.register(Tip)
admin.site.register(SubmittedTip)
admin.site.register(UserProfile)




