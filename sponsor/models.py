from django.contrib.auth import get_user_model
from django.db import models
from school.models import FundingCampaign


class BaseModel(models.Model):
    user = get_user_model()

    created_by = models.ForeignKey(
        user,
        on_delete=models.CASCADE,
    )
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Sponsor(BaseModel):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="logo/sponsors/", blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images/sponsor/", blank=True)

    def __str__(self):
        return self.name


class SponsorRepresentative(BaseModel):
    role = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(
        upload_to="images/sponsor/representative/", blank=True)

    sponsor_company = models.ForeignKey(
        "Sponsor", on_delete=models.CASCADE, related_name="representative", blank=True
    )

    def __str__(self):
        return self.email


class Donation(BaseModel):
    funding_campaign = models.ForeignKey(
        to=FundingCampaign,
        on_delete=models.PROTECT,
        related_name="donations",
    )
    sponsor_org = models.ForeignKey(
        "Sponsor", on_delete=models.PROTECT, related_name="donations"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.sponsor_org.name

    def create(self, *args, **kwargs):
        self.created_by = self.request.user
        return super().create(*args, **kwargs)


class AnonymousDonation(models.Model):
    funding_campaign = models.ForeignKey(
        to=FundingCampaign,
        on_delete=models.PROTECT,
        related_name="anonymous_donations",
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()

    created_by = models.CharField(
        max_length=200, blank=True, default="Anonymous User", editable=False
    )

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Anonymous - {self.amount}"
