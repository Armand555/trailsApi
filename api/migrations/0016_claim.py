# Generated by Django 3.2.5 on 2021-08-02 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_listing_trail_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('trail_email', models.EmailField(blank=True, max_length=256)),
                ('claim_expiry', models.DateTimeField(default=datetime.datetime(2021, 8, 3, 12, 28, 48, 189930))),
            ],
        ),
    ]
