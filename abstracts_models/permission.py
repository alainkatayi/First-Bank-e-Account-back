from rest_framework import permissions

class IsAdminOrAgent(permissions.BasePermission):

    def has_permission(self, request, view):

        #on verifie si le user est connecté
        if not request.user or not request.user.is_authenticated:
            return False
        
        #on verifie le role
        return request.user.role in ['admin', 'agent']