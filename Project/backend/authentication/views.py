from django.conf import settings
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


def home(request):
    return render(request, "home.html")


def login_with_turnstile(request):
    """Render login page with Turnstile"""
    context = {
        "site_key": getattr(settings, "TURNSTILE_SITE_KEY", ""),
    }
    return render(request, "authentication/login.html", context)


@api_view(["GET"])
def get_jwt_token(request):
    if not request.user.is_authenticated:
        return Response({"error": "Please sign in first"}, status=401)
    refresh = RefreshToken.for_user(request.user)
    return Response(
        {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
    )
