from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import UserTrailLinking, Listing, Claim, UserProfile
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode


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


class CountMyTrailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTrailLinking
        fields = ['trail']


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


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', ' uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)

        return super().validate(attrs)


class InvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
