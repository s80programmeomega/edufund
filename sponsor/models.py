from django.db import models

from school.models import FundingCampaign


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="sponsors", blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SponsorRepresentative(models.Model):
    role = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(
        upload_to="images/school/representative/", blank=True)

    sponsor = models.ForeignKey(
        "Sponsor", on_delete=models.CASCADE, related_name="representative", blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Donation(models.Model):
    funding_campaign = models.ForeignKey(
        to=FundingCampaign, on_delete=models.PROTECT, related_name="donations")
    sponsor = models.ForeignKey(
        "Sponsor", on_delete=models.PROTECT, related_name="donations")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sponsor.name
