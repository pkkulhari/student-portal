from django.urls import path

from base.views import index, login, logout, register, dashboard, userUpdate, userDelete

app_name = "base"
urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path("user/<int:pk>/update/", userUpdate, name="user-update"),
    path("user/<int:pk>/delete/", userDelete, name="user-delete"),
    path("dashboard/", dashboard, name="dashboard"),
]
