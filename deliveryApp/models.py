from django.db import models


class Delivery_my_stuff(models.Model):
    my_departure_lat = models.FloatField()  # 출발 위도
    my_departure_long = models.FloatField()  # 출발 경도
    my_departure_addr = models.CharField(max_length=100)  # 출발 상세주소
    my_departure_phone = models.IntegerField()  # 보내는 이 폰번호
    my_destination_lat = models.FloatField()  # 도착 위도
    my_destination_long = models.FloatField()  # 도착 경도
    my_destination_addr = models.CharField(max_length=100)  # 도착 상세주소
    my_destination_phone = models.IntegerField()  # 받는 이 폰번호
    my_created = models.DateTimeField(auto_now_add=True)  # 현재시간
    my_limit_time = models.CharField(max_length=100)  # 제한시간
    my_goods = models.CharField(max_length=100)  # 상품 카테고리
    my_goodsinfo = models.CharField(max_length=30)  # 상품 상세정보
    my_weigth = models.FloatField()  # 상품 무게
    my_distance = models.IntegerField()  # 상품 거리
    my_price = models.IntegerField()  # 상품 가격
    my_content = models.CharField(max_length=30)  # 상품


class Delivery_market(models.Model):
    mar_departure_lat = models.FloatField()
    mar_departure_long = models.FloatField()
    mar_departure_addr = models.CharField(max_length=100)
    mar_departure_phone = models.IntegerField()
    mar_destination_lat = models.FloatField()
    mar_destination_long = models.FloatField()
    mar_destination_addr = models.CharField(max_length=100)
    mar_destination_phone = models.IntegerField()
    mar_item = models.CharField(max_length=100)
    mar_created = models.DateTimeField(auto_now_add=True)
    mar_limit_time = models.CharField(max_length=100)
    mar_weight = models.FloatField()
    mar_distance = models.IntegerField()
    mar_price = models.IntegerField()
    mar_content = models.CharField(max_length=30)


mar_departure_lat = models.FloatField()
mar_departure_long = models.FloatField()
mar_departure_addr = models.CharField(max_length=100)
mar_departure_phone = models.IntegerField()
mar_destination_lat = models.FloatField()
mar_destination_long = models.FloatField()
mar_destination_addr = models.CharField(max_length=100)
mar_destination_phone = models.IntegerField()
mar_item = models.CharField(max_length=100)
mar_created = models.DateTimeField(auto_now_add=True)
mar_limit_time = models.CharField(max_length=100)
mar_weight = models.FloatField()
mar_distance = models.IntegerField()
mar_price = models.IntegerField()
mar_content = models.CharField(max_length=30)
mar_departure_lat = models.FloatField()
mar_departure_long = models.FloatField()
mar_departure_addr = models.CharField(max_length=100)
mar_departure_phone = models.IntegerField()
mar_destination_lat = models.FloatField()
mar_destination_long = models.FloatField()
mar_destination_addr = models.CharField(max_length=100)
mar_destination_phone = models.IntegerField()
mar_item = models.CharField(max_length=100)
mar_created = models.DateTimeField(auto_now_add=True)
mar_limit_time = models.CharField(max_length=100)
mar_weight = models.FloatField()
mar_distance = models.IntegerField()
mar_price = models.IntegerField()
mar_content = models.CharField(max_length=30)
mar_departure_lat = models.FloatField()
mar_departure_long = models.FloatField()
mar_departure_addr = models.CharField(max_length=100)
mar_departure_phone = models.IntegerField()
mar_destination_lat = models.FloatField()
mar_destination_long = models.FloatField()
mar_destination_addr = models.CharField(max_length=100)
mar_destination_phone = models.IntegerField()
mar_item = models.CharField(max_length=100)
mar_created = models.DateTimeField(auto_now_add=True)
mar_limit_time = models.CharField(max_length=100)
mar_weight = models.FloatField()
mar_distance = models.IntegerField()
mar_price = models.IntegerField()
mar_content = models.CharField(max_length=30)
