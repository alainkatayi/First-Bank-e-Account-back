from rest_framework import permissions

class IsAdminOrAgent(permissions.BasePermission):

    def has_permission(self, request, view):

        #on verifie si le user est connecté
        if not request.user or not request.user.is_authenticated:
            return False
        
        #on verifie le role
        return request.user.role in ['admin', 'agent']

class IsAdminUserRole(permissions.BasePermission):
    """
    Permet l'accès uniquement aux utilisateurs ayant le rôle 'admin'.
    """
    def has_permission(self, request, view):
        # On vérifie si l'utilisateur est authentifié ET si son rôle est admin
        return bool(request.user and request.user.is_authenticated and request.user.role == 'admin')