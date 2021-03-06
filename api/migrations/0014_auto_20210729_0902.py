# Generated by Django 3.2.5 on 2021-07-29 07:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0013_rename_owner_usertraillinking'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usertraillinking',
            unique_together={('user', 'trail')},
        ),
        migrations.AlterIndexTogether(
            name='usertraillinking',
            index_together={('user', 'trail')},
        ),
    ]
