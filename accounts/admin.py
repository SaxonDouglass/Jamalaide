from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from accounts.models import Profile, Team, CommitteeMember, ContactLink

class ProfileInline(admin.TabularInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Team)
admin.site.register(CommitteeMember)
admin.site.register(ContactLink)
