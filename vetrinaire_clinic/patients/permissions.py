from rest_framework import permissions

class IsVetOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Bloque la suppression ici, on gère ça dans la permission suivante
        if request.method == 'DELETE':
            return False
        return request.user.is_authenticated and request.user.role in ['admin', 'vet']

class IsAdminDeleteOnly(permissions.BasePermission):
    """
    Seul l'admin peut supprimer (DELETE).
    """
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.is_authenticated and request.user.role == 'admin'
        return True