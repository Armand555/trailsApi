# Generated by Django 3.2.5 on 2021-08-02 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20210802_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='claim_expiry',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 12, 48, 17, 102228)),
        ),
        migrations.AlterField(
            model_name='claim',
            name='claim_token',
            field=models.IntegerField(default=736734, unique=True),
        ),
    ]