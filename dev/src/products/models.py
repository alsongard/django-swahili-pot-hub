from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120, null=False)
    price = models.DecimalField(max_digits=10000, null=False, blank=False, decimal_places=2)
    description = models.TextField(blank=False, null=False)
    summary = models.TextField(default='This is cool!')
    feature = models.BooleanField(default=True)

