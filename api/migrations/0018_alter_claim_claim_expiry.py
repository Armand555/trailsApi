# Generated by Django 3.2.5 on 2021-08-02 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_claim_claim_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='claim_expiry',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 12, 38, 38, 852699)),
        ),
    ]
