from rest_framework import permissions


class IsOwnerOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        elif request.user == view.get_object().owner:
            return True
        else:
            return False
