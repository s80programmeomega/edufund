from rest_framework import permissions, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)
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
        if self.action in {'list', 'retrieve'}:
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [
                permissions.IsAuthenticated, permissions.IsAdminUser,]
        return [permission() for permission in self.permission_classes]


# class TokenViewSet(viewsets.ViewSet):
#     @action(detail=False, methods=['post'])
#     def token(self, request):
#         return TokenObtainPairView.as_view()(request)

#     @action(detail=False, methods=['post'])
#     def refresh(self, request):
#         return TokenRefreshView.as_view()(request)

#     @action(detail=False, methods=['post'])
#     def verify(self, request):
#         return TokenVerifyView.as_view()(request)

#     @action(detail=False, methods=['post'])
#     def get_urls(self):
#         urls = [
#             path('token/', self.get_token, name='token_obtain_pair'),
#             path('token/refresh/', self.refresh_token, name='token_refresh'),
#             path('token/verify/', self.verify_token, name='token_verify'),
#         ]
#         return urls
