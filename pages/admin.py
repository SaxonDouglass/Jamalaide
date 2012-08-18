from django.contrib import admin
from pages.models import Page

class PageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Page, PageAdmin)
