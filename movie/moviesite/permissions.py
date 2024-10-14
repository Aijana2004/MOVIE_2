from rest_framework import permissions


class CheckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
            # return obj.owner == request.user

        if request.user.status('Pro') and obj.status_choices('Pro'):
            return True
        if request.user.status("Simple") and obj.status_choices('Simple'):
            return True
        return False
