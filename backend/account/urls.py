from django.urls import path
from .views import Logout, Login, Register, ChangePassword,Profile


app_name = 'account'

urlpatterns = [
    path("login/", Login, name="login"),
    path("logout/", Logout, name="logout"),
    path("register/", Register, name="register"),
    path("change_password/", ChangePassword, name="changePassword"),
    path("profile/", Profile, name="profile"),

]
