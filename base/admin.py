from django.contrib import admin
from .models import Event,Booking

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'participant_name', 'event', 'num_tickets', 'booking_date')

admin.site.register(Event)
admin.site.register(Booking)
