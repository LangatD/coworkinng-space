from django.db import models

class CoworkingSpace(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    available_seats = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
