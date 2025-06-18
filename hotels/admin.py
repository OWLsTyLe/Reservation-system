from django.contrib import admin
from .models import Hotel, RoomType, HotelRoom

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'image', 'address', 'get_price_per_night')
    search_fields = ('name', 'address')

    def get_price_per_night(self, obj):
        return obj.hotel_rooms.first().price_per_night if obj.hotel_rooms.exists() else "N/A"
    get_price_per_night.short_description = 'Price Per Night'

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'room_type', 'price_per_night', 'available_count')
    search_fields = ('hotel', 'room_type')
