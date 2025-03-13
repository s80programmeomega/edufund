from rest_framework import serializers

import school
from sponsor.models import Sponsor

from .models import (
    FundingCampaign,
    Representative,
    School,
    SchoolDocument,
    SchoolImage,
    Student,
)


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = [
            "pk",
            "id_number",
            "name",
            "location",
            "address",
            "description",
        ]


class RepresentativeSerializer(serializers.ModelSerializer):

    school = serializers.HyperlinkedRelatedField(
        view_name="school-detail", queryset=School.objects.all()
    )

    class Meta:
        model = Representative
        fields = [
            "pk",
            "id_number",
            "first_name",
            "last_name",
            "email",
            "phone",
            "photo",
            "school",
        ]


class StudentSerializer(serializers.ModelSerializer):

    school = serializers.HyperlinkedRelatedField(
        view_name="school-detail", queryset=School.objects.all()
    )

    class Meta:
        model = Student
        fields = [
            "pk",
            "first_name",
            "last_name",
            "student_class",
            "student_story",
            "phone",
            "photo",
            "parent_consent",
            "school",
        ]


class FundingCampaignSerializer(serializers.ModelSerializer):

    schools = serializers.HyperlinkedRelatedField(
        view_name="school-detail", queryset=School.objects.all(), many=True
    )

    sponsors = serializers.HyperlinkedRelatedField(
        view_name="sponsor-detail",
        queryset=Sponsor.objects.all(),
        many=True,
    )

    funding_progression = serializers.SerializerMethodField(method_name="get_funding_progression" ,read_only=True)

    def get_funding_progression(self, obj: FundingCampaign):
        return obj.funding_progression

    class Meta:
        model = FundingCampaign
        fields = [
            "pk",
            "name",
            "amount",
            "reason",
            "description",
            "schools",
            "sponsors",
            "funding_progression",
            "status",
            "start_date",
            "end_date",
        ]
        read_only_fields = [
            "funding_progression",
        ]

class SchoolDocumentSerializer(serializers.ModelSerializer):

    school = serializers.HyperlinkedRelatedField(
        view_name="school-detail", queryset=School.objects.all()
    )

    class Meta:
        model = SchoolDocument
        fields = "__all__"
        read_only_fields = ["date_added", "last_modified"]


class SchoolImageSerializer(serializers.ModelSerializer):

    school = serializers.HyperlinkedRelatedField(
        view_name="school-detail", queryset=School.objects.all()
    )

    class Meta:
        model = SchoolImage
        fields = "__all__"
        read_only_fields = ["date_added", "last_modified"]
