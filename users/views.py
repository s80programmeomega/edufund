from rest_framework import permissions, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)
from rest_framework import authentication
from rest_framework.decorators import action
from django.urls import path

from .models import CustomUser as User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_field = 'id'

    def get_permissions(self):
        """Grant permission based on action.

        Returns:
            permissions: a list of permissions.
        """
        if self.action == "create" and self.request.user.is_anonymous:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ["list", "update", "partial_update", "destroy"]:
            self.permission_classes = [permissions.IsAdminUser,]
        elif self.action == "retrieve":
            self.permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in self.permission_classes]
