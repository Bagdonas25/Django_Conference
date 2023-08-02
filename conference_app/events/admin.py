from django.contrib import admin
from events.models import Event, CompanyRegistration

class CompanyRegistrationAdmin( admin.ModelAdmin ):
    list_display = [ "company_name", "event_title", "people_count" ]

    def event_title(self, model):
        return f"Renginys: {model.event.title}"


# Register your models here.
admin.site.register(Event)
admin.site.register(CompanyRegistration, CompanyRegistrationAdmin)