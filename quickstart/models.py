from django.db import models

class Role(models.Model):
    company = models.CharField(max_length=20)
    role_name =  models.CharField(max_length=20)

class Role_permission(models.Model):
    role = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)
    permission_name = models.CharField(max_length=20, default='read')

class Login(models.Model):
    username = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)
