# Generated by Django 3.2.5 on 2021-07-29 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0011_auto_20210729_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell', models.IntegerField()),
                ('postal_address', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=50)),
                ('province', models.CharField(choices=[('NU', '<-- Select Province -->'), ('GA', 'Gauteng'), ('FS', 'Free State'), ('KN', 'KwaZulu-Natal'), ('WC', 'Western Cape'), ('NC', 'Northern Cape'), ('EC', 'Eastern Cape'), ('LP', 'Limpopo'), ('MP', 'Mpumalanga'), ('NW', 'North West')], default='NU', max_length=2)),
                ('code', models.IntegerField()),
                ('reg_no', models.CharField(blank=True, max_length=14)),
                ('vat_no', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
