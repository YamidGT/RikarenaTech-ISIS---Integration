from django.urls import include, path

from . import views

urlpatterns = [
    # OAuth login/logout (allauth)
    path("auth/", include("allauth.urls")),
    # Custom login with Turnstile
    path("login/", views.login_with_turnstile, name="login_with_turnstile"),
]
