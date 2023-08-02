from django.contrib import admin
from conferences.models import Conference, Comment
from events.models import Event


class EventInline(admin.TabularInline):
    model = Event
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "start_date", "end_date"]
    inlines = [EventInline]


admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Comment)
