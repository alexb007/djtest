from rest_framework import permissions

from core.models import Application


class ApiKeyPermission(permissions.BasePermission):
    message = 'API_KEY is not exists or invalid'

    def has_permission(self, request, view):

        api_key = (request.data if request.method == 'post' else request.query_params).get('api_key', None)
        if api_key:
            permission = Application.objects.filter(api_key=api_key, is_active=True).exists()
            return permission
        return False
