<<<<<<< HEAD
from django.contrib import admin

# Register your models here.

from MainApp.models import Tip
from MainApp.models import UserProfile

admin.site.register(Tip)
admin.site.register(UserProfile)
=======
from django.contrib import admin

# Register your models here.

from MainApp.models import Tip, UserProfile, BlogEntry

admin.site.register(Tip)
admin.site.register(UserProfile)

class BlogEntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(BlogEntry, BlogEntryAdmin)
>>>>>>> 2e6026cdfe1357ee2587c1d0aeb8f7300ad9f20a
