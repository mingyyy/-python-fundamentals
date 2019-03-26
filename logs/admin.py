from django.contrib import admin
from .models import Topic, Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ("topic_id", "text", "date_added")


class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "date_added")

# Register your models here.
admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)