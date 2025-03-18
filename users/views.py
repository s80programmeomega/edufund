from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, generics
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser as User
from .serializers import LoginSerializer, LogoutSerializer, UserSerializer


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


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(generics.GenericAPIView):
    """Handle  user login"""

    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

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


@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(generics.GenericAPIView):
    """Handle user logout"""

    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response(
                {'error': 'Invalid or expired token'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except KeyError:
            return Response(
                {'error': 'Refresh token not provided'},
                status=status.HTTP_400_BAD_REQUEST
            )
