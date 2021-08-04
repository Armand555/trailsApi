from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/listings/normal', views.ListingsFree.as_view()),
    path('api/listings/premium', views.ListingsPremium.as_view()),

    path('api/listings/normal/create', views.AddFreeListing.as_view()),
    path('api/listings/premium/create', views.AddPremiumListing.as_view()),

    path('api/my_trails', views.MyTrails.as_view()),
    path('api/my_trails/delete/<int:pk>/', views.ReleaseMyTrail.as_view()),

    path('api/my_trails/normal/update/<int:pk>/', views.UpdateFreeListing.as_view()),
    path('api/my_trails/premium/update/<int:pk>/', views.UpdatePremiumListing.as_view()),

    re_path('^api/listings/normal/prov/(?P<province>.+)/$', views.ProvinceListingsFree.as_view()),
    re_path('^api/listings/premium/prov/(?P<province>.+)/$', views.ProvinceListingsPremium.as_view()),

    re_path('^api/listings/normal/id/(?P<id>.+)/$', views.IdListingsFree.as_view()),
    re_path('^api/listings/premium/id/(?P<id>.+)/$', views.IdListingsPremium.as_view()),

    path('api/claim/', views.ClaimView.as_view()),

    path('api/claim/y/<int:pk>/<int:token>', views.ConfirmClaimView.as_view()),
    path('api/claim/n/<int:pk>/<int:token>', views.DeclineClaimView.as_view()),

    path('api-auth/', include('rest_framework.urls')),
    path('api/change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    path('api/contact', TemplateView.as_view(template_name="home.html"), name='home'),
    path('request-reset-email', views.RequestPasswordResetEmail.as_view(), name='request-reset-email'),

    path('password-reset/<uidb64>/<token>/', views.PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),

    path('api/signup', views.signup),
    path('api/login', views.login),
]
