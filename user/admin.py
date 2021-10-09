from django.contrib import admin

# Register your models here.
from user.models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'status')
    list_filter = ('status', )
