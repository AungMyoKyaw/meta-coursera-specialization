from django.db import models

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField(null=True, blank=True)
    reservation_slot = models.CharField(max_length=50, default='', blank=True)

    class Meta:
        unique_together = ('reservation_date', 'reservation_slot')

    def __str__(self):
        return f"{self.first_name} - {self.reservation_date} at {self.reservation_slot}"


class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField(null=False)
   menu_item_description = models.TextField(max_length=1000, default='')

   def __str__(self):
      return self.name
