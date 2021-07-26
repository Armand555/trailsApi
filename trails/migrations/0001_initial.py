# Generated by Django 3.2.5 on 2021-07-26 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail', models.CharField(max_length=36)),
                ('trail_owner', models.CharField(max_length=36)),
                ('area', models.CharField(max_length=36)),
                ('province', models.CharField(max_length=36)),
                ('trail_length', models.IntegerField()),
                ('elevation_gain', models.IntegerField()),
                ('route_type', models.CharField(choices=[('LO', 'Loop'), ('OB', 'Out And Back'), ('PP', 'Point to Point')], default='LO', max_length=2)),
                ('trail_type', models.CharField(choices=[('DT', 'Day trail'), ('SP', 'Slack pack'), ('BP', 'Backpack'), ('LD', 'Long distance'), ('WN', 'Wilderness'), ('BC', 'Basecamp')], default='DT', max_length=2)),
                ('trail_difficulty', models.CharField(choices=[('BR', 'Breeze'), ('EZ', 'Easy'), ('IN', 'Intermediate'), ('HA', 'Hard'), ('EX', 'Extreme')], default='BR', max_length=2)),
                ('about', models.TextField()),
                ('accommodation', models.TextField()),
                ('pertinent_info', models.TextField()),
                ('main_image', models.TextField()),
                ('pet_friendly', models.IntegerField()),
                ('birding', models.IntegerField()),
                ('fly_fishing', models.IntegerField()),
                ('abseiling', models.IntegerField()),
                ('horse_riding', models.IntegerField()),
                ('trail_running', models.IntegerField()),
                ('mountain_biking', models.IntegerField()),
                ('guided', models.IntegerField()),
                ('river_rafting', models.IntegerField()),
                ('off_road', models.IntegerField()),
            ],
        ),
    ]