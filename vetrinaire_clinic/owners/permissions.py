from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)

class IsAdminOrVetOrReadOnly(permissions.BasePermission):
    """
    Seuls les admins ou vétérinaires peuvent ajouter/modifier, les autres peuvent juste lire.
    """
    def has_permission(self, request, view):
        # Log authentication status
        logger.info(f"User authenticated: {request.user.is_authenticated}")
        logger.info(f"User role: {request.user.role}")
        logger.info(f"Request method: {request.method}")
        
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return (
            request.user.is_authenticated and 
            request.user.role in ['admin', 'vet']
        )

class IsAdminDeleteOnly(permissions.BasePermission):
    """
    Seul l'admin peut supprimer (DELETE).
    """
    def has_permission(self, request, view):
        # Log delete permission check
        logger.info(f"Checking delete permission for user: {request.user.username}")
        logger.info(f"User role: {request.user.role}")
        logger.info(f"Request method: {request.method}")
        
        if request.method == 'DELETE':
            has_perm = request.user.is_authenticated and request.user.role == 'admin'
            logger.info(f"Delete permission granted: {has_perm}")
            return has_perm
        return True
