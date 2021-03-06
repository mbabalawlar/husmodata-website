# Generated by Django 3.1 on 2021-08-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtuapp', '0004_auto_20210810_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='affillate_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='network',
            name='corporate_data_vending_medium',
            field=models.CharField(choices=[('UWS', 'UWS'), ('SMS', 'SMS'), ('MSORG_DEVELOPED_WEBSITE', 'MSORG_DEVELOPED_WEBSITE'), ('SMEPLUG', 'SMEPLUG')], max_length=30),
        ),
    ]
