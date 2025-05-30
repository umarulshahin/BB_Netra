from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission): 
    
    def has_permission(self, request, view):
        
        print("Checking if user is authenticated and is a superuser")
        # Check if the user is authenticated and is a superuser
        return request.user and request.user.is_authenticated and request.user.is_superuser