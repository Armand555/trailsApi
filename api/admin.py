from django.contrib import admin
from .models import Listing, UserTrailLinking, UserProfile, Claim

admin.site.register(UserProfile)
admin.site.register(Claim)


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['trail', 'trail_owner']
    list_filter = ['route_type', 'trail_type']
    search_fields = ['trail', 'trail_owner']


@admin.register(UserTrailLinking)
class UserTrailLinkingAdmin(admin.ModelAdmin):
    list_display = ['trail', 'user']
    search_fields = ['user__username', 'trail__trail']
