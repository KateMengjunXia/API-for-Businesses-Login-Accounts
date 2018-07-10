from rest_framework import viewsets
from BusinessAccounts.quickstart.serializers import LoginSerializer, RoleSerializer, Role_permissionSerializer
from BusinessAccounts.quickstart.models import Login, Role, Role_permission

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('company')
    serializer_class = RoleSerializer

class Role_permissionViewSet(viewsets.ModelViewSet):
    queryset = Role_permission.objects.all().order_by('role')
    serializer_class = Role_permissionSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all().order_by('role')
    serializer_class = LoginSerializer

