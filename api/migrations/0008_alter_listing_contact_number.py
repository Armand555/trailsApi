# Generated by Django 3.2.5 on 2021-07-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_listing_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='contact_number',
            field=models.IntegerField(null=True),
        ),
    ]
