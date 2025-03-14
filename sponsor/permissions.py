from rest_framework import permissions


class IsSponsor(permissions.BasePermission):
    """Authorize only sponsor type user or admin"""
    def __init__(self):
        self.user_types = ["sponsor", "admin"]

    def has_permission(self, request, view):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return False

        # Check if user has the required user_type
        return str(request.user.user_type).lower() in self.user_types

    def has_object_permission(self, request, view, obj):
        return str(request.user.user_type).lower() in self.user_types
