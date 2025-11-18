from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Items(models.Model):
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)