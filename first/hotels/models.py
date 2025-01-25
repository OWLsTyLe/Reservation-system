from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='', blank=True, null=True)
    description = models.TextField(max_length=500)
    rating = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    address = models.CharField(max_length=200, default='Unknown address')  # Переконайтесь, що це поле існує
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name

class RoomType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

class HotelRoom(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_rooms')
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='hotel_rooms')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    total_count = models.PositiveIntegerField()
    available_count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.room_type.name} - ({self.hotel.name}) - {self.price_per_night} грн"
