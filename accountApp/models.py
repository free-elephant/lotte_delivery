from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 유저랑 1:1관계
    player_name = models.CharField(max_length=10)
    player_nickname = models.CharField(max_length=10, blank=True, null=True)
    player_security_number = models.IntegerField(blank=True, null=True)
    player_email = models.CharField(max_length=30, blank=True, null=True)
    player_latitude = models.FloatField(blank=True, null=True)  # 위도
    # 경도
    player_longtitude = models.FloatField(blank=True, null=True)
    player_address = models.CharField(max_length=30, blank=True, null=True)
    player_detail_addr = models.CharField(
        max_length=20, blank=True, null=True)  # 상세 주소
    player_sale_coupon = models.CharField(max_length=30, blank=True, null=True)
    player_phone = models.IntegerField(blank=True, null=True)  # 휴대폰번호

    def __str__(self):
        n_user = str(self.user)
        return n_user


@receiver(post_save, sender=User)  # 자동으로 생성
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()
