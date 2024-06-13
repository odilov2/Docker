from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()

    class Meta:
        db_table = 'product'
