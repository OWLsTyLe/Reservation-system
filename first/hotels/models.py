from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='', blank=True, null=True)
    description = models.TextField(max_length=500)
    rating = models.DecimalField(max_digits=5, decimal_places=1,default=0.0)

    def __str__(self):
        return self.name