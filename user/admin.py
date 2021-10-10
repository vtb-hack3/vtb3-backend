from django.contrib import admin

# Register your models here.
from user.models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'coins', 'status')
    list_filter = ('status', )
