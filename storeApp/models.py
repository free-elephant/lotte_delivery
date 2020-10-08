from django.db import models


class Store(models.Model):
    store_name = models.CharField(max_length=30)
    store_lat = models.FloatField()
    store_long = models.FloatField()
    store_addr = models.CharField(max_length=100)
    store_phone = models.IntegerField()
    store_goods = models.ManyToManyField(
        'Good', related_name='goods', blank=True)


class Good(models.Model):
    good_name = models.CharField(max_length=30)
    good_price = models.IntegerField()
    good_weight = models.FloatField()
