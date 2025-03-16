from rest_framework import viewsets
from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly, AllowAny)

from school.models import (FundingCampaign, Representative, School,
                           SchoolDocument, SchoolImage, Student)
from school.permissions import IsSchool
from school.serializers import (FundingCampaignSerializer,
                                RepresentativeSerializer,
                                SchoolDocumentSerializer,
                                SchoolImageSerializer, SchoolSerializer,
                                StudentSerializer)


class SchoolViewSet(viewsets.ModelViewSet):
    model = School
    lookup_field = "pk"
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsSchool]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()


class RepresentativeViewSet(viewsets.ModelViewSet):
    model = Representative
    lookup_field = "pk"
    queryset = Representative.objects.all()
    serializer_class = RepresentativeSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsSchool]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()


class StudentViewSet(viewsets.ModelViewSet):
    model = Student
    lookup_field = "pk"
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsSchool]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()


class FundingCampaignViewSet(viewsets.ModelViewSet):
    model = FundingCampaign
    lookup_field = "pk"
    queryset = FundingCampaign.objects.all()
    serializer_class = FundingCampaignSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsSchool]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()


class SchoolDocumentViewSet(viewsets.ModelViewSet):
    model = SchoolDocument
    lookup_field = "pk"
    queryset = SchoolDocument.objects.all()
    serializer_class = SchoolDocumentSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsSchool]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()


class SchoolImageViewSet(viewsets.ModelViewSet):
    model = SchoolImage
    lookup_field = "pk"
    queryset = SchoolImage.objects.all()
    serializer_class = SchoolImageSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsSchool]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()
