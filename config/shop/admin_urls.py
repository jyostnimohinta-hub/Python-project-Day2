from django.urls import path
from . import admin_views

urlpatterns = [
    path("login/", admin_views.admin_login, name="admin_login"),
    path("dashboard/", admin_views.admin_dashboard, name="admin_dashboard"),
    path("logout/", admin_views.admin_logout, name="admin_logout"),
]