# Generated by Django 3.1.2 on 2020-10-25 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=30, null=True)),
                ('goods_category', models.CharField(max_length=30, null=True)),
                ('goods_price', models.IntegerField()),
                ('goods_weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=30)),
                ('store_lat', models.FloatField()),
                ('store_image', models.ImageField(blank=True, upload_to='')),
                ('store_lng', models.FloatField()),
                ('store_addr', models.CharField(max_length=100)),
                ('store_phone', models.IntegerField(blank=True, null=True)),
                ('store_goods', models.ManyToManyField(blank=True, related_name='goods', to='storeApp.Goods')),
            ],
        ),
    ]
