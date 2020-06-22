from django.conf import settings
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

from apps.api.views import ObtainAuthToken
from apps.api.views import TelegramView

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
        description="The API is the API",
        terms_of_service="TBD",
        contact=openapi.Contact(email=settings.EMAIL_FROM),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path("", include("apps.api.impl.urls")),
    path("tg/", csrf_exempt(TelegramView.as_view())),
    path("obtain_auth_token/", ObtainAuthToken.as_view(), name="obtain_auth_token"),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]