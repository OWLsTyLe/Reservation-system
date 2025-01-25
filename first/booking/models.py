from django.db import models
from hotels.models import HotelRoom
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(HotelRoom, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        room_info = self.room if self.room else "Unknown Room"
        user_info = self.user.username if self.user else "Anonymous"
        return f'Booking by {user_info} for {room_info}'
