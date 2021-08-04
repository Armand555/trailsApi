from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserTrailLinking, Listing, Claim


class NormalListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'trail', 'area', 'province', 'contact_number', 'contact_email', 'premium']


class PremiumListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'trail', 'area', 'province', 'contact_number', 'contact_email', 'premium', 'premium_expiry',
                  'active', 'pet_friendly', 'birding', 'fly_fishing', 'abseiling', 'horse_riding', 'trail_running',
                  'mountain_biking', 'guided', 'river_rafting', 'off_road']


class MyTrailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTrailLinking
        fields = '__all__'


class UserTrailLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTrailLinking
        fields = '__all__'


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'


class AddPremiumListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class AddFreeListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'trail', 'area', 'province', 'contact_number', 'contact_email', 'active', 'premium']


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class RequestPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=9)

    class Meta:
        fields = ['email']
