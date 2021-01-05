from rest_framework.permissions import BasePermission


class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'ngo'


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'user'
