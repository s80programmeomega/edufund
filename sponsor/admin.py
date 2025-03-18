from django.contrib import admin

from .models import Donation, AnonymousDonation, Sponsor, SponsorRepresentative

admin.site.register(AnonymousDonation)


class BaseAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not change:  # If this is a new object (not an edit)
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


class DonationInline(admin.TabularInline):
    model = Donation
    extra = 1
    list_display = ['amount', 'funding_campaign']


class SponsorRepresentativeInline(admin.TabularInline):
    model = SponsorRepresentative
    extra = 1


@admin.register(Sponsor)
class SponsorAdmin(BaseAdmin):
    list_display = ['name', 'email', 'phone', 'date_added', 'last_modified']
    search_fields = ['name', 'email']
    inlines = [DonationInline,  SponsorRepresentativeInline]


@admin.register(Donation)
class DonationAdmin(BaseAdmin):
    list_display = ['sponsor', 'funding_campaign', 'amount']
    list_filter = ['sponsor', 'funding_campaign']
    search_fields = ['sponsor__name', 'funding_campaign__name']
