'''
Created on Feb 9, 2015

@author: mzy
'''
from rest_framework.permissions import DjangoModelPermissions


class AccessPermissions(DjangoModelPermissions):
    
    def has_permission(self, request, view):
        user = request.user
        if user.is_anonymous() and not getattr(view, 'allow_anonymous', False):
            return False
        return True
