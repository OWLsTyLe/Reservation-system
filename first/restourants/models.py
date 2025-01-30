from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='', blank=True, null=True)
    description = models.TextField(max_length=1000)
    rating = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    address = models.CharField(max_length=200, default='Unknown address')
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tables')
    number = models.PositiveIntegerField()
    seats = models.PositiveIntegerField(default=4)

    class Meta:
        unique_together = ("restaurant", "number")

    def __str__(self):
        return f"Столики {self.number} - ({self.restaurant.name})"

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="reservations")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("table", "date", "time")

    def __str__(self):
        return f"{self.user.username} - {self.table} на {self.date} о {self.time}"