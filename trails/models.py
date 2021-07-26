from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Listing(models.Model):
    class RouteType(models.TextChoices):
        LOOP = 'LO', _('Loop')
        OUT_AND_BACK = 'OB', _('Out And Back')
        POINT_TO_POINT = 'PP', _('Point to Point')

    class TrailType(models.TextChoices):
        DAY_TRAIL = 'DT', _('Day trail')
        SLACK_PACK = 'SP', _('Slack pack')
        BACKPACK = 'BP', _('Backpack')
        LONG_DISTANCE = 'LD', _('Long distance')
        WILDERNESS = 'WN', _('Wilderness')
        BASECAMP = 'BC', _('Basecamp')

    class TrailDifficulty(models.TextChoices):
        BREEZE = 'BR', _('Breeze')
        EASY = 'EZ', _('Easy')
        INTERMEDIATE = 'IN', _('Intermediate')
        HARD = 'HA', _('Hard')
        EXTREME = 'EX', _('Extreme')

    trail = models.CharField(max_length=36)
    trail_owner = models.CharField(max_length=36)
    area = models.CharField(max_length=36)
    province = models.CharField(max_length=36)
    trail_length = models.IntegerField()
    elevation_gain = models.IntegerField()
    route_type = models.CharField(
        max_length=2,
        choices=RouteType.choices,
        default=RouteType.LOOP,
    )
    trail_type = models.CharField(
        max_length=2,
        choices=TrailType.choices,
        default=TrailType.DAY_TRAIL,
    )
    trail_difficulty = models.CharField(
        max_length=2,
        choices=TrailDifficulty.choices,
        default=TrailDifficulty.BREEZE,
    )
    about = models.TextField()
    accommodation = models.TextField()
    rates = []
    pertinent_info = models.TextField()
    main_image = models.TextField()
    carousel_images = []
    pet_friendly = models.IntegerField()
    birding = models.IntegerField()
    fly_fishing = models.IntegerField()
    abseiling = models.IntegerField()
    horse_riding = models.IntegerField()
    trail_running = models.IntegerField()
    mountain_biking = models.IntegerField()
    guided = models.IntegerField()
    river_rafting = models.IntegerField()
    off_road = models.IntegerField()
