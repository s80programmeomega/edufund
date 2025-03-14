from django.contrib import admin

from .models import Donation, Sponsor, SponsorRepresentative


class DonationInline(admin.TabularInline):
    model = Donation
    extra = 1
    list_display = ['amount', 'funding_campaign']

class SponsorRepresentativeInline(admin.TabularInline):
    model = SponsorRepresentative
    extra = 1

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date_added', 'last_modified']
    search_fields = ['name', 'email']
    inlines = [DonationInline,  SponsorRepresentativeInline]


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['sponsor', 'funding_campaign', 'amount']
    list_filter = ['sponsor', 'funding_campaign']
    search_fields = ['sponsor__name', 'funding_campaign__name']
