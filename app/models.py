from django.db import models

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='my_images/', blank=True, null=True)
    category = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'Items'
