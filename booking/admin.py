from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'start_date', 'end_date', 'created_at')
    list_filter = ('room', 'start_date', 'end_date')
    search_fields = ('user__username', 'room__hotel__name')

admin.site.register(Booking, BookingAdmin)
