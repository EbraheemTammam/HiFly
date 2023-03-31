from rest_framework.permissions import BasePermission


class AdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.admin
            or request.user.is_staff 
            or request.method == 'GET'
        )

class Admin(BasePermission):
    def has_permission(self, request, view):
        return request.user.admin or request.user.is_staff