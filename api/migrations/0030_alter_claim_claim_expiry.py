# Generated by Django 3.2.5 on 2021-08-03 06:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_alter_claim_claim_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='claim_expiry',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 4, 6, 53, 33, 361881, tzinfo=utc)),
        ),
    ]
