from django.contrib import admin
from .models import Restaurant

admin.site.register(Restaurant)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'image')
    search_fields = ('description')

