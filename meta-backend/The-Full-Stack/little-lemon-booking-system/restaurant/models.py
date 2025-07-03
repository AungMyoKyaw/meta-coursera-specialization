from django.db import models
from django.conf import settings

class Booking(models.Model):
    full_name = models.CharField(max_length=200, db_column='first_name')  # preserve existing DB column
    reservation_date = models.DateField(null=True, blank=True)
    reservation_slot = models.CharField(max_length=50, default='', blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bookings'
    )

    class Meta:
        unique_together = ('reservation_date', 'reservation_slot')

    def __str__(self):
        return f"{self.full_name} - {self.reservation_date} at {self.reservation_slot}"


class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField(null=False)
   menu_item_description = models.TextField(max_length=1000, default='')

   def __str__(self):
      return self.name
