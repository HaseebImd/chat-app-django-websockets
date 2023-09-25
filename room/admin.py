from django.contrib import admin

# Register your models here.
from .models import Room, Message

class AdminRoom(admin.ModelAdmin):
    list_display = ["name", "slug", "created", "updated"]
    prepopulated_fields = {"slug": ("name",)}

class AdminMessage(admin.ModelAdmin):
    list_display = ["room", "content", "user", "date_added"]



admin.site.register(Room, AdminRoom)
admin.site.register(Message, AdminMessage)