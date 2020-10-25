# Generated by Django 3.1.2 on 2020-10-25 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery_my_stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_departure_lat', models.FloatField()),
                ('my_departure_long', models.FloatField()),
                ('my_departure_address', models.CharField(max_length=100)),
                ('my_departure_addr', models.CharField(max_length=100)),
                ('my_departure_phone', models.IntegerField()),
                ('my_departure_name', models.CharField(blank=True, max_length=10, null=True)),
                ('my_destination_lat', models.FloatField()),
                ('my_destination_long', models.FloatField()),
                ('my_destination_address', models.CharField(max_length=100)),
                ('my_destination_addr', models.CharField(max_length=100)),
                ('my_destination_name', models.CharField(blank=True, max_length=10, null=True)),
                ('my_destination_phone', models.IntegerField()),
                ('my_date', models.DateField(blank=True, null=True)),
                ('my_time', models.CharField(blank=True, max_length=20, null=True)),
                ('my_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('my_goods', models.CharField(max_length=100)),
                ('my_goodsinfo', models.CharField(max_length=30)),
                ('my_weigth', models.FloatField()),
                ('my_distance', models.IntegerField()),
                ('my_price', models.IntegerField()),
                ('my_content', models.CharField(max_length=30)),
                ('my_complete_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('my_message', models.CharField(blank=True, max_length=40, null=True)),
                ('deliver_stuff_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deliver_stuff_user', to=settings.AUTH_USER_MODEL)),
                ('stuff_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stuff_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery_market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mar_departure_lat', models.FloatField()),
                ('mar_departure_long', models.FloatField()),
                ('mar_departure_address', models.CharField(blank=True, max_length=100, null=True)),
                ('mar_departure_addr', models.CharField(max_length=100)),
                ('mar_departure_phone', models.IntegerField(blank=True, null=True)),
                ('mar_item', models.CharField(max_length=1000)),
                ('mar_count', models.CharField(max_length=1000)),
                ('mar1_departure_lat', models.FloatField(blank=True, null=True)),
                ('mar1_departure_long', models.FloatField(blank=True, null=True)),
                ('mar1_departure_address', models.CharField(blank=True, max_length=100, null=True)),
                ('mar1_departure_addr', models.CharField(blank=True, max_length=100, null=True)),
                ('mar1_departure_phone', models.IntegerField(blank=True, null=True)),
                ('mar1_item', models.CharField(blank=True, max_length=1000, null=True)),
                ('mar1_count', models.CharField(blank=True, max_length=1000, null=True)),
                ('mar2_departure_lat', models.FloatField(blank=True, null=True)),
                ('mar2_departure_long', models.FloatField(blank=True, null=True)),
                ('mar2_departure_address', models.CharField(blank=True, max_length=100, null=True)),
                ('mar2_departure_addr', models.CharField(blank=True, max_length=100, null=True)),
                ('mar2_departure_phone', models.IntegerField(blank=True, null=True)),
                ('mar2_item', models.CharField(blank=True, max_length=1000, null=True)),
                ('mar2_count', models.CharField(blank=True, max_length=1000, null=True)),
                ('mar3_departure_lat', models.FloatField(blank=True, null=True)),
                ('mar3_departure_long', models.FloatField(blank=True, null=True)),
                ('mar3_departure_address', models.CharField(blank=True, max_length=100, null=True)),
                ('mar3_departure_addr', models.CharField(blank=True, max_length=100, null=True)),
                ('mar3_departure_phone', models.IntegerField(blank=True, null=True)),
                ('mar3_item', models.CharField(blank=True, max_length=1000, null=True)),
                ('mar3_count', models.CharField(blank=True, max_length=1000, null=True)),
                ('mar_destination_lat', models.FloatField()),
                ('mar_destination_long', models.FloatField()),
                ('mar_destination_address', models.CharField(blank=True, max_length=100, null=True)),
                ('mar_destination_addr', models.CharField(max_length=100)),
                ('mar_destination_name', models.CharField(blank=True, max_length=10, null=True)),
                ('mar_destination_phone', models.IntegerField(blank=True, null=True)),
                ('mar_date', models.DateField(blank=True, null=True)),
                ('mar_time', models.CharField(max_length=20)),
                ('mar_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('mar_weight', models.FloatField()),
                ('mar_distance', models.IntegerField(blank=True, null=True)),
                ('mar_price', models.IntegerField()),
                ('mar_content', models.CharField(blank=True, max_length=30, null=True)),
                ('mar_complete_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('mar_message', models.CharField(blank=True, max_length=40, null=True)),
                ('deliver_mar_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deliver_mar_user', to=settings.AUTH_USER_MODEL)),
                ('mar_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mar_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
