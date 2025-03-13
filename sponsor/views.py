from rest_framework import viewsets

from .serializers import (
    SponsorSerializer,
    SponsorRepresentativeSerializer,
    DonationSerializer,
)
from .models import Sponsor, SponsorRepresentative, Donation


class SponsorViewSet(viewsets.ModelViewSet):
    model = Sponsor
    lookup_field = "pk"
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorRepresentativeViewSet(viewsets.ModelViewSet):
    model = SponsorRepresentative
    lookup_field = "pk"
    queryset = SponsorRepresentative.objects.all()
    serializer_class = SponsorRepresentativeSerializer


class DonationViewSet(viewsets.ModelViewSet):
    model = Donation
    lookup_field = "pk"
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
