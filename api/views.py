import random

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Listing, Claim, UserTrailLinking, UserProfile
from .serializers import NormalListingsSerializer, PremiumListingSerializer, ClaimSerializer, UserTrailLinkSerializer, \
    MyTrailsSerializer, AddPremiumListingSerializer, AddFreeListingSerializer, ChangePasswordSerializer, \
    RequestPasswordResetEmailSerializer, SetNewPasswordSerializer, CountMyTrailsSerializer, InvoiceDetailsSerializer

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from .utils import Util


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(data['username'], password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token),
                                 'message': 'Your account was successfully created.'
                                            ' You may now login, no need for activation'},
                                status=201)
        except IntegrityError:
            return JsonResponse({'error': 'That username has already been taken.'}, status=400)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error': 'Could not login. Please check username and password'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=200)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = RequestPasswordResetEmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data.get('email', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relative_link = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            redirect_url = request.data.get('redirect_url', '')
            absurl = 'http://' + current_site + relative_link
            email_body = 'Hello, \n Use link below to reset your password  \n' + \
                         absurl + "?redirect_url=" + redirect_url
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your password'}
            Util.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    def get(self, request, uidb64, token):

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new one'},
                                status=status.HTTP_401_UNAUTHORIZED)
            return Response({'success': True, 'message': 'Credentials Valid', 'uidb64': uidb64, 'token': token},
                            status=status.HTTP_200_OK)
        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error': 'Token is not valid, please request a new one'},
                                status=status.HTTP_401_UNAUTHORIZED)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)


class ListingsFree(generics.ListAPIView):
    serializer_class = NormalListingsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Listing.objects.filter(premium=False)


class ListingsPremium(generics.ListAPIView):
    serializer_class = PremiumListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Listing.objects.filter(premium=True)


class ProvinceListingsPremium(generics.ListAPIView):
    serializer_class = PremiumListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        province = self.kwargs['province']
        return Listing.objects.filter(province=province).filter(premium=True)


class ProvinceListingsFree(generics.ListAPIView):
    serializer_class = NormalListingsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        province = self.kwargs['province']
        return Listing.objects.filter(province=province).filter(premium=False)


class IdListingsPremium(generics.ListAPIView):
    serializer_class = PremiumListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        id_num = self.kwargs['id']
        return Listing.objects.filter(id=id_num).filter(premium=True)


class IdListingsFree(generics.ListAPIView):
    serializer_class = NormalListingsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        id_num = self.kwargs['id']
        return Listing.objects.filter(id=id_num).filter(premium=False)


class ClaimView(generics.CreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        random_token = random.randint(100001, 999999)
        serializer.save(claim_token=random_token)


class ConfirmClaimView(generics.CreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = UserTrailLinkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        claim = Claim.objects.get(pk=self.kwargs['pk'], claim_token=self.kwargs['token'])

        if self.request.user.id == claim.user_id:
            if timezone.now() < claim.claim_expiry:
                listing_id = claim.trail_id
                serializer.save(trail=Listing.objects.get(pk=listing_id), user=self.request.user)
            else:
                return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class DeclineClaimView(generics.RetrieveDestroyAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        Claim.objects.filter(pk=kwargs['pk'], claim_token=self.kwargs['token']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MyTrails(generics.ListAPIView):
    serializer_class = MyTrailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        links = UserTrailLinking.objects.filter(user_id=self.request.user.id)
        return links


class MyFreeTrails(generics.ListAPIView):
    serializer_class = CountMyTrailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        links = UserTrailLinking.objects.values_list('trail', flat=True)
        trail = Listing.objects.filter(pk__in=links, premium=False)
        return trail


# def premium_rate(request):
#     total_trails = MyTrails()
#     if total_trails == 1:
#         price_per_trail = 600
#     elif total_trails == 2:
#         price_per_trail = 540
#     elif total_trails == 3:
#         price_per_trail = 480
#     else:
#         price_per_trail = 420
#
#     return price_per_trail


class ReleaseMyTrail(generics.DestroyAPIView):
    queryset = UserTrailLinking.objects.all()
    serializer_class = MyTrailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        UserTrailLinking.objects.filter(pk=kwargs['pk']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InvoiceDetails(generics.ListAPIView):
    serializer_class = InvoiceDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id_num = self.kwargs['id']
        return UserProfile.objects.filter(user=id_num)


class AddPremiumListing(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = AddPremiumListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddFreeListing(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = AddFreeListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdatePremiumListing(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = AddPremiumListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

    def delete(self, request, *args, **kwargs):
        Listing.objects.filter(pk=kwargs['pk']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateFreeListing(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = AddFreeListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

    def delete(self, request, *args, **kwargs):
        Listing.objects.filter(pk=kwargs['pk']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
