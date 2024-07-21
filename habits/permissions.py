from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ Пермишн для владельца """

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False
