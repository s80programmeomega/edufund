from django.shortcuts import render
from rest_framework import viewsets

from school.models import (
    FundingCampaign,
    Representative,
    School,
    SchoolDocument,
    SchoolImage,
    Student,
)
from school.serializers import (
    FundingCampaignSerializer,
    RepresentativeSerializer,
    SchoolDocumentSerializer,
    SchoolImageSerializer,
    SchoolSerializer,
    StudentSerializer,
)


class SchoolViewSet(viewsets.ModelViewSet):
    model = School
    lookup_field = "pk"
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class RepresentativeViewSet(viewsets.ModelViewSet):
    model = Representative
    lookup_field = "pk"
    queryset = Representative.objects.all()
    serializer_class = RepresentativeSerializer


class StudentViewSet(viewsets.ModelViewSet):
    model = Student
    lookup_field = "pk"
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class FundingCampaignViewSet(viewsets.ModelViewSet):
    model = FundingCampaign
    lookup_field = "pk"
    queryset = FundingCampaign.objects.all()
    serializer_class = FundingCampaignSerializer


class SchoolDocumentViewSet(viewsets.ModelViewSet):
    model = SchoolDocument
    lookup_field = "pk"
    queryset = SchoolDocument.objects.all()
    serializer_class = SchoolDocumentSerializer


class SchoolImageViewSet(viewsets.ModelViewSet):
    model = SchoolImage
    lookup_field = "pk"
    queryset = SchoolImage.objects.all()
    serializer_class = SchoolImageSerializer
