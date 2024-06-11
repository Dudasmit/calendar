from django.contrib import admin
from core.models import Apointments, Winkel, TypeEvent

# Register your models here.
#admin.site.register(Apointments)
admin.site.register(Winkel)
admin.site.register(TypeEvent)


@admin.register(Apointments)
class CalendarAdmin(admin.ModelAdmin):
    list_filter  = ["winkel","start_time"]