# Generated by Django 3.1 on 2021-04-23 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supershop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='quantity',
            field=models.IntegerField(verbose_name='количество'),
        ),
    ]
