# Generated by Django 3.1 on 2020-10-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='store_phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
