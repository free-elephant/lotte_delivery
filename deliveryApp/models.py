from django.db import models
from storeApp.models import Goods


class Delivery_my_stuff(models.Model):  # 내 물건 배송
    my_departure_lat = models.FloatField()  # 출발 위도
    my_departure_long = models.FloatField()  # 출발 경도
    my_departure_addr = models.CharField(max_length=100)  # 출발 상세주소
    my_departure_phone = models.IntegerField()  # 보내는 이 폰번호
    my_destination_lat = models.FloatField()  # 도착 위도
    my_destination_long = models.FloatField()  # 도착 경도
    my_destination_addr = models.CharField(max_length=100)  # 도착 상세주소
    my_destination_phone = models.IntegerField()  # 받는 이 폰번호

    my_date = models.DateField()  # 날짜 설정
    my_time = models.CharField(max_length=20)  # 시간 설정

    my_created = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)  # 현재시간
    # my_limit_time = models.CharField(
    #     max_length=100, blank=True, null=True)  # 제한시간
    my_goods = models.CharField(max_length=100)  # 상품 카테고리
    my_goodsinfo = models.CharField(max_length=30)  # 상품 상세정보
    my_weigth = models.FloatField()  # 상품 무게
    my_distance = models.IntegerField()  # 상품 거리
    my_price = models.IntegerField()  # 상품 가격

    my_content = models.CharField(max_length=30)  # 상품


class Delivery_market(models.Model):  # 가게물건 배송
    mar_departure_lat = models.FloatField()  # 첫번째 가게 위도
    mar_departure_long = models.FloatField()  # 첫번째 가게 경도
    mar_departure_addr = models.CharField(max_length=100)  # 출발지 상세주소
    mar_departure_phone = models.IntegerField()  # 출발지 전화번호
    mar_item = models.ManyToManyField(
        'storeApp.Goods', related_name='first_goods')

    mar1_departure_lat = models.FloatField(blank=True, null=True)  # 두번째 가게 위도
    mar1_departure_long = models.FloatField(blank=True, null=True)  # 두번째 가게 경도
    mar1_departure_addr = models.CharField(
        max_length=100, blank=True, null=True)  # 두번째 가게 상세주소
    mar1_departure_phone = models.IntegerField(
        blank=True, null=True)  # 출발지 전화번호
    mar1_item = models.ManyToManyField(
        'storeApp.Goods', related_name='seconde_goods', blank=True)  # 아이템

    mar2_departure_lat = models.FloatField(blank=True, null=True)  # 세번째 가게 위도
    mar2_departure_long = models.FloatField(blank=True, null=True)  # 세번째 가게 경도
    mar2_departure_addr = models.CharField(
        max_length=100, blank=True, null=True)  # 세번째 가게 상세주소
    mar2_departure_phone = models.IntegerField(
        blank=True, null=True)  # 출발지 전화번호
    mar2_item = models.ManyToManyField(
        'storeApp.Goods', related_name='third_goods', blank=True)  # 아이템

    mar3_departure_lat = models.FloatField(blank=True, null=True)  # 네 번째 가게 위도
    mar3_departure_long = models.FloatField(blank=True, null=True)  # 네번째 가게 경도
    mar3_departure_addr = models.CharField(
        max_length=100, blank=True, null=True)  # 네번째 가게 상세주소
    mar3_departure_phone = models.IntegerField(
        blank=True, null=True)  # 네번째 가게 전화번호
    mar3_item = models.ManyToManyField(
        'storeApp.Goods', related_name='fourth_goods', blank=True)

    mar_destination_lat = models.FloatField()  # 도착지 위도
    mar_destination_long = models.FloatField()  # 도착지 경도
    mar_destination_addr = models.CharField(max_length=100)  # 도착지 상세주소
    mar_destination_phone = models.IntegerField()  # 도착지 전화번호

    mar_date = models.DateField(blank=True, null=True)  # 날짜 설정
    mar_time = models.CharField(max_length=20)  # 시간 설정

    mar_created = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)  # 현재 시간

    mar_weight = models.FloatField()  # 물건 무게
    mar_distance = models.IntegerField()  # 출발지-도착지 거리
    mar_price = models.IntegerField()  # 배송비
    mar_content = models.CharField(max_length=30)  # 전달사항
