from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

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
        if self.action in {'list', 'retrieve'}:
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [
                permissions.IsAuthenticated, permissions.IsAdminUser,]
        return [permission() for permission in self.permission_classes]
