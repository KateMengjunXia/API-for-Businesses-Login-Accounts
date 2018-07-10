from django.conf.urls import url, include
from rest_framework import routers
from BusinessAccounts.quickstart import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'roles', views.RoleViewSet)
router.register(r'role_permissions', views.Role_permissionViewSet)
router.register(r'logins', views.LoginViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls))
]
