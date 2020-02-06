from django.contrib import admin

# Register your models here.

from .models import Player, Room

admin.site.site_header = 'Administrator'
admin.site.site_title = 'Lock Industries Admin Area'
admin.site.index_title = 'Welcome to the Admin Area'

class RoomInLine(admin.TabularInline):
    model = Room


class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['currentRoom']}),
    ({'User': ['user'], 'Unique': ['uuid']}),]
    inlines = [Room]



admin.site.register(Player)
admin.site.register(Room)