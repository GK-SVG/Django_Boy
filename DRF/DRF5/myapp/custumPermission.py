from rest_framework.authentication import BaseAuthentication

class MyPermission(BaseAuthentication):
    def has_permission(self,request,view):
        print('request--',request)
        print('view--',view)
        if request.method=='GET':
            return True
        return False