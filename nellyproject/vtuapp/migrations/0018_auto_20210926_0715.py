# Generated by Django 3.1 on 2021-09-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtuapp', '0017_auto_20210926_0705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info_alert',
            name='disable',
        ),
        migrations.AddField(
            model_name='info_alert',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='alert_images'),
        ),
        migrations.AlterField(
            model_name='info_alert',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='network',
            name='corporate_data_vending_medium',
            field=models.CharField(choices=[('SMS', 'SMS'), ('USSD', 'USSD'), ('CG_KONNECT', 'CG_KONNECT'), ('MSORG_DEVELOPED_WEBSITE', 'MSORG_DEVELOPED_WEBSITE'), ('UWS', 'UWS'), ('SMEPLUG', 'SMEPLUG')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='network',
            name='gifting_data_vending_medium',
            field=models.CharField(choices=[('SMS', 'SMS'), ('USSD', 'USSD'), ('CG_KONNECT', 'CG_KONNECT'), ('MSORG_DEVELOPED_WEBSITE', 'MSORG_DEVELOPED_WEBSITE'), ('UWS', 'UWS'), ('SMEPLUG', 'SMEPLUG')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='result_checker_pin',
            name='provider_api',
            field=models.CharField(choices=[('MOBILENIG', 'MOBILENIG'), ('VTPASS', 'VTPASS'), ('EASYACCESS', 'EASYACCESS.COM.NG')], default='MOBILENIG', max_length=30),
        ),
    ]