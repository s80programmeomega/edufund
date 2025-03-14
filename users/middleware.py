# users/middleware.py
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest
# or from .anonymous import CustomAnonymousUser
from .models import CustomAnonymousUser


class AnonymousUserTypeMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        if not request.user.is_authenticated:
            request.user = CustomAnonymousUser()
            request.user.__setattr__("user_type", "Guest")
        return None
