# Generated by Django 3.2.5 on 2021-08-02 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20210802_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='claim_expiry',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 13, 11, 17, 30460)),
        ),
        migrations.AlterField(
            model_name='claim',
            name='claim_token',
            field=models.IntegerField(unique=True),
        ),
    ]
