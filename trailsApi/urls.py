from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api import views

schema_view = get_schema_view(
    openapi.Info(
        title="SA Hiking Trails API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.sahikingtrails.co.za/policies/terms/",
        contact=openapi.Contact(email="contact@sahikingtrails.co.za"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/listings/normal', views.ListingsFree.as_view()),
    path('api/listings/premium', views.ListingsPremium.as_view()),

    path('api/listings/normal/create', views.AddFreeListing.as_view()),
    path('api/listings/premium/create', views.AddPremiumListing.as_view()),

    path('api/my_trails', views.MyTrails.as_view()),
    path('api/my_free_trails', views.MyFreeTrails.as_view()),

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

    re_path('api/profile/(?P<id>.+)/$', views.InvoiceDetails.as_view()),

    path('api/change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('request-reset-email', views.RequestPasswordResetEmail.as_view(), name='request-reset-email'),

    path('password-reset/<uidb64>/<token>/', views.PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', views.SetNewPasswordAPIView.as_view(), name='password-reset-complete'),

    path('api/signup', views.signup),
    path('api/login', views.login),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
