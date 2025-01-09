from django.contrib import admin
from .models import Hotel

admin.site.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'image')
    search_fields = ('description')

