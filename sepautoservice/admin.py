from django.contrib import admin
from .models import  Service_Apointments

# Register your models here.
#admin.site.register(Service_Apointments)

@admin.register(Service_Apointments)
class CalendarAdmin(admin.ModelAdmin):
    list_filter  = ["naam", "datum"]
