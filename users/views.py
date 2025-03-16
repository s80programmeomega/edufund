from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)
from rest_framework import authentication
from rest_framework.decorators import action
from django.urls import path

from .models import CustomUser as User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate


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



def get_tokens_for_user(user):
    """Generate user token"""
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class LoginView(APIView):
    """Handle  user login"""

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user:
            tokens = get_tokens_for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'tokens': tokens,
                'message': 'Login Successful'
            }, status=status.HTTP_200_OK)

        return Response({
            'error': 'Invalid Credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)
