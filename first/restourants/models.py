from django.db import models
class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='', blank=True, null=True)
    description = models.TextField(max_length=1000)
    rating = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)

    def __str__(self):
        return self.name

