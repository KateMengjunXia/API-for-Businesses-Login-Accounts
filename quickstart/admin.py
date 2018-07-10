from django.contrib import admin
from BusinessAccounts.quickstart.models import Login, Role, Role_permission

admin.site.register(Login)
admin.site.register(Role)
admin.site.register(Role_permission)
