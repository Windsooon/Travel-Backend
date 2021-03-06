from rest_framework import permissions
from rest_framework.compat import is_authenticated


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS or
            request.user and
            is_authenticated(request.user) and request.user.is_staff
        )
