from rest_framework import serializers

from .models import AnonymousDonation, Sponsor, Donation, SponsorRepresentative


class SponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
        fields = "__all__"
        read_only_fields = ["date_added", "last_modified"]


class SponsorRepresentativeSerializer(serializers.ModelSerializer):

    sponsor = serializers.HyperlinkedRelatedField(
        view_name="sponsor-detail", queryset=Sponsor.objects.all()
    )

    class Meta:
        model = SponsorRepresentative
        fields = "__all__"
        read_only_fields = ["date_added", "last_modified"]


class DonationSerializer(serializers.ModelSerializer):

    sponsor = serializers.HyperlinkedRelatedField(
        view_name="sponsor-detail", queryset=Sponsor.objects.all()
    )

    class Meta:
        model = Donation
        fields = "__all__"
        read_only_fields = ["date_added", "last_modified"]


class AnonymousDonationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnonymousDonation
        fields = "__all__"
        read_only_fields = ["date_added", "last_modified"]
