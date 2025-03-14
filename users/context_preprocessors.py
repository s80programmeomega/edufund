import http
from django.http import HttpRequest


def set_anonymous_user_type(request: HttpRequest):
    """Set anonymous user type to guest"""
    user = request.user
    if not user.is_authenticated:
        user.__setattr__("user_type", "Guest")
    return {"user_type": user.user_type}