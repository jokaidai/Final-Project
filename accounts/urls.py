from django.urls import path
from .views import (
    signup, 
    signin, 
    signout,
    update_profile,
    profile
    )

urlpatterns = [
    path("signup", signup, name = 'signup'),
    path("signin", signin, name = "signin"),
    path("signout", signout, name = "signout"),
    path("update-profile", update_profile, name = "update_profile"),
    path("user-profile", profile, name = "profile")
]