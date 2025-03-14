from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny

from sponsor.permissions import IsSponsor

from .models import Donation, Sponsor, SponsorRepresentative, AnonymousDonation
from .serializers import (AnonymousDonationSerializer, DonationSerializer, SponsorRepresentativeSerializer,
                          SponsorSerializer)


class SponsorViewSet(viewsets.ModelViewSet):
    model = Sponsor
    lookup_field = "pk"
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsSponsor]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in self.permission_classes]


class SponsorRepresentativeViewSet(viewsets.ModelViewSet):
    model = SponsorRepresentative
    lookup_field = "pk"
    queryset = SponsorRepresentative.objects.all()
    serializer_class = SponsorRepresentativeSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsSponsor]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in self.permission_classes]


class DonationViewSet(viewsets.ModelViewSet):
    model = Donation
    lookup_field = "pk"
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsSponsor]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in self.permission_classes]


class AnonymousDonationViewSet(viewsets.ModelViewSet):
    model = AnonymousDonation
    lookup_field = "pk"
    queryset = AnonymousDonation.objects.all()
    serializer_class = AnonymousDonationSerializer

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]
