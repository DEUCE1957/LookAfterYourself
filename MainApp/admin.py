from django.contrib import admin

# Register your models here.

from MainApp.models import Tip, UserProfile, BlogEntry

admin.site.register(Tip)
admin.site.register(UserProfile)

class BlogEntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(BlogEntry, BlogEntryAdmin)
