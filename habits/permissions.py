from rest_framework.permissions import BasePermission


class OwnerPermission(BasePermission):
    """Право доступа пользователя, владелец"""
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user