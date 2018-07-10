from rest_framework import serializers
from BusinessAccounts.quickstart.models import Login, Role, Role_permission

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('company', 'role_name')
	
class Role_permissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role_permission
        fields = ('role', 'permission_name')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('username', 'password', 'last_name', 'first_name', 'role')
        extra_kwargs = {'password': {'write_only': True}}
