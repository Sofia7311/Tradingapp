from django.db import models
from mainapp.models import CustomUser
from django.utils import timezone

# Create your models here.
class AddressHistory(models.Model):
    home_address                =   models.CharField(max_length = 200, verbose_name = 'New Address')
    home_address_move_date      =   models.DateField(default=timezone.now, verbose_name = 'Date Moved In')
    home_address_move_out_date  =   models.DateField(blank=True, null=True, verbose_name = 'Date Moved Out')
    addresshistory              =   models.ForeignKey(CustomUser, on_delete = models.CASCADE, blank=True, verbose_name = 'Updated by')

    class Meta:
        ordering = ['addresshistory_id', 'home_address_move_date']

    def __str__(self):
        return self.home_address

