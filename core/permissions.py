from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'


class IsResident(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'resident'


class IsSecurity(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'security'