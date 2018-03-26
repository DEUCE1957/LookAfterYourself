from django.contrib import admin

# Register your models here.

from MainApp.models import Tip, Submission, Suggestion
from MainApp.models import UserProfile
from MainApp.models import Service
from MainApp.models import Post


admin.site.register(Tip)
admin.site.register(Submission)
admin.site.register(UserProfile)
admin.site.register(Service)
admin.site.register(Suggestion)
admin.site.register(Post)



