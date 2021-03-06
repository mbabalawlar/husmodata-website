# Generated by Django 3.1 on 2021-09-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtuapp', '0009_auto_20210826_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='cgkonnect_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='network',
            name='corporate_data_vending_medium',
            field=models.CharField(choices=[('CG_KONNECT', 'CG_KONNECT'), ('UWS', 'UWS'), ('USSD', 'USSD'), ('MSORG_DEVELOPED_WEBSITE', 'MSORG_DEVELOPED_WEBSITE'), ('SMEPLUG', 'SMEPLUG'), ('SMS', 'SMS')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='network',
            name='gifting_data_vending_medium',
            field=models.CharField(choices=[('CG_KONNECT', 'CG_KONNECT'), ('UWS', 'UWS'), ('USSD', 'USSD'), ('MSORG_DEVELOPED_WEBSITE', 'MSORG_DEVELOPED_WEBSITE'), ('SMEPLUG', 'SMEPLUG'), ('SMS', 'SMS')], max_length=30, null=True),
        ),
    ]
