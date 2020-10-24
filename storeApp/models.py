from django.db import models


class Store(models.Model):
    store_name = models.CharField(max_length=30)
    store_lat = models.FloatField()
    store_image = models.ImageField(blank=True)
    store_lng = models.FloatField()
    store_addr = models.CharField(max_length=100)
    store_phone = models.IntegerField(blank=True, null=True)
    store_goods = models.ManyToManyField(
        'Goods', related_name='goods', blank=True)

    def __str__(self):
        return self.store_name


class Goods(models.Model):
    goods_name = models.CharField(max_length=30, null=True)
    goods_category = models.CharField(max_length=30, null=True)
    goods_price = models.IntegerField()
    goods_weight = models.FloatField()

    def __str__(self):
        return self.goods_name  # 함수는 문제없는0
