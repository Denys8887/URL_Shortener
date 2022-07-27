from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from url_shortener_api.views import Redirector

schema_view = get_schema_view(
    openapi.Info(
        title="UrlShortener",
        default_version="v1",
        description="UrlShortener",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("api/", include("url_shortener_api.urls", namespace="api")),
    path("<str:shortener_link>/", Redirector.as_view(), name="redirector"),
]
