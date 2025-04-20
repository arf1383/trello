from rest_framework import permissions

class IsBoardAdmin(permissions.BasePermission):
    """
    اجازه فقط به اعضای گروه 'board_admin' برای دسترسی کامل.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='board_admin').exists()