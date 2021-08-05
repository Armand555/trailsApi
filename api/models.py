from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone


class Listing(models.Model):
    class RouteType(models.TextChoices):
        NULL = 'NU', _('<-- Select Type -->')
        LOOP = 'LO', _('Loop')
        OUT_AND_BACK = 'OB', _('Out And Back')
        POINT_TO_POINT = 'PP', _('Point to Point')

    class TrailType(models.TextChoices):
        NULL = 'NU', _('<-- Select Type -->')
        DAY_TRAIL = 'DT', _('Day trail')
        SLACK_PACK = 'SP', _('Slack pack')
        BACKPACK = 'BP', _('Backpack')
        LONG_DISTANCE = 'LD', _('Long distance')
        WILDERNESS = 'WN', _('Wilderness')
        BASECAMP = 'BC', _('Basecamp')

    class TrailDifficulty(models.TextChoices):
        NULL = 'NU', _('<-- Select Difficulty -->')
        BREEZE = 'BR', _('Breeze')
        EASY = 'EZ', _('Easy')
        INTERMEDIATE = 'IN', _('Intermediate')
        HARD = 'HA', _('Hard')
        EXTREME = 'EX', _('Extreme')

    class Province(models.TextChoices):
        NULL = 'NU', _('<-- Select Province -->')
        GAUTENG = 'GA', _('Gauteng')
        FREE_STATE = 'FS', _('Free State')
        KWAZULU_NATAL = 'KN', _('KwaZulu-Natal')
        WESTERN_CAPE = 'WC', _('Western Cape')
        NORTHERN_CAPE = 'NC', _('Northern Cape')
        EASTERN_CAPE = 'EC', _('Eastern Cape')
        LIMPOPO = 'LP', _('Limpopo')
        MPUMALANGA = 'MP', _('Mpumalanga')
        NORTH_WEST = 'NW', _('North West')

    trail = models.CharField(max_length=36, blank=False, unique=True)
    trail_owner = models.CharField(max_length=36)
    area = models.CharField(max_length=36, blank=False)
    province = models.CharField(
        max_length=2,
        choices=Province.choices,
        default=Province.NULL,
    )
    trail_length = models.FloatField()
    elevation_gain = models.IntegerField(blank=True)
    route_type = models.CharField(
        max_length=2,
        choices=RouteType.choices,
        default=RouteType.NULL,
    )
    trail_type = models.CharField(
        max_length=2,
        choices=TrailType.choices,
        default=TrailType.NULL,
    )
    trail_difficulty = models.CharField(
        max_length=2,
        choices=TrailDifficulty.choices,
        default=TrailDifficulty.NULL,
    )
    about = models.TextField(blank=True)
    accommodation = models.TextField(blank=True)
    rates = []
    pertinent_info = models.TextField(blank=True)
    main_image = models.ImageField(upload_to='main_image/', blank=True)
    carousel_images = []
    pet_friendly = models.BooleanField(default=False)
    birding = models.BooleanField(default=False)
    fly_fishing = models.BooleanField(default=False)
    abseiling = models.BooleanField(default=False)
    horse_riding = models.BooleanField(default=False)
    trail_running = models.BooleanField(default=False)
    mountain_biking = models.BooleanField(default=False)
    guided = models.BooleanField(default=False)
    river_rafting = models.BooleanField(default=False)
    off_road = models.BooleanField(default=False)
    contact_number = models.IntegerField(null=True)
    contact_email = models.EmailField(max_length=256, blank=True)
    location_pin = models.CharField(max_length=256, blank=True)
    listing_date = models.DateField(auto_now_add=True, blank=True, null=True)
    active = models.BooleanField(default=True)
    premium = models.BooleanField(default=False)
    premium_expiry = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.trail


class UserTrailLinking(models.Model):
    trail = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'trail'),)
        index_together = (('user', 'trail'),)


class UserProfile(models.Model):
    class Province(models.TextChoices):
        NULL = 'NU', _('<-- Select Province -->')
        GAUTENG = 'GA', _('Gauteng')
        FREE_STATE = 'FS', _('Free State')
        KWAZULU_NATAL = 'KN', _('KwaZulu-Natal')
        WESTERN_CAPE = 'WC', _('Western Cape')
        NORTHERN_CAPE = 'NC', _('Northern Cape')
        EASTERN_CAPE = 'EC', _('Eastern Cape')
        LIMPOPO = 'LP', _('Limpopo')
        MPUMALANGA = 'MP', _('Mpumalanga')
        NORTH_WEST = 'NW', _('North West')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cell = models.IntegerField(blank=False)
    postal_address = models.CharField(max_length=100, blank=False)
    area = models.CharField(max_length=50, blank=False)
    province = models.CharField(
        max_length=2,
        choices=Province.choices,
        default=Province.NULL,
    )
    code = models.IntegerField(blank=False)
    reg_no = models.CharField(max_length=14, blank=True)
    vat_no = models.CharField(max_length=10, blank=True)


class Claim(models.Model):
    trail_id = models.IntegerField(blank=False)
    user_id = models.IntegerField(blank=False)
    trail_email = models.EmailField(max_length=256, blank=True)
    claim_token = models.IntegerField(unique=True, default=False)
    claim_expiry = models.DateTimeField(default=timezone.now() + timedelta(days=1))


class Invoice(models.Model):
    invoice_num = models.IntegerField(blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total = models.IntegerField(blank=False)
    invoice_date = models.DateTimeField(default=timezone.now())
    paid = models.BooleanField(default=False)
    trails = models.TextField(blank=False)
    invoice_url = models.ImageField(upload_to='invoice/', blank=True)
