from jams.models import *
from django.contrib import admin

@admin.register(Jam)
class JamAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(JamAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].initial = request.user
        return form

class GameResourceInline(admin.TabularInline):
    model = GameResource

class GameAdmin(admin.ModelAdmin):
    inlines = [
        GameResourceInline,
    ]

admin.site.register(Game, GameAdmin)
admin.site.register(GameResource)
