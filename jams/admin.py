from jams.models import *
from django.contrib import admin

admin.site.register(Jam)

class GameResourceInline(admin.TabularInline):
    model = GameResource

class GameAdmin(admin.ModelAdmin):
    inlines = [
        GameResourceInline,
    ]

admin.site.register(Game, GameAdmin)
admin.site.register(GameResource)
