from django.db import models

# Create your models here.

class Items(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)

    # class Meta:
    #     verbose_name_plural = 'Items'
