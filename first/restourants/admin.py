from django.contrib import admin
from .models import Restaurant,Table, Reservation

admin.site.register(Restaurant)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'image')
    search_fields = ('description')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("number", "restaurant", "seats")
    list_filter = ("restaurant",)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("user", "table", "date", "time")
    list_filter = ("date", "table__restaurant")
    search_fields = ("user__username", "table__restaurant__name")

