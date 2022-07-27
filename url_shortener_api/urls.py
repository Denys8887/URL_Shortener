from django.urls import path

from url_shortener_api.views import (ShortenerCreateApiView,
                                     ShortenerListAPIView,
                                     UnshortenerCreateApiView,
                                     UnshortenerListAPIView)

app_name = "api"

urlpatterns = [
    path("", ShortenerListAPIView.as_view(), name="shortening_list"),
    path("shortening/", ShortenerCreateApiView.as_view(), name="shortening_link"),
    path("unshortener/", UnshortenerCreateApiView.as_view(), name="unshortener_link"),
    path("unshortenlist/", UnshortenerListAPIView.as_view(), name="unshorten_list"),
]
