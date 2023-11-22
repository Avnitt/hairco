from rest_framework.permission import BasePermission

class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'client'

    def has_object_permission(self, request, view, obj):
        return True

