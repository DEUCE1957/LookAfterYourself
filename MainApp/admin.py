from django.contrib import admin

# Register your models here.

from MainApp.models import Tip, SubmittedTip
from MainApp.models import UserProfile,Service

admin.site.register(Tip)
admin.site.register(SubmittedTip)
admin.site.register(UserProfile)
admin.site.register(Service)




