from django.shortcuts import redirect
from django.views import View
from rest_framework.generics import ListAPIView, CreateAPIView
from django.conf import settings

from url_shortener_api.models import Link
from url_shortener_api.serializers import LinkSerializer, UnshortenerSerializer


class ShortenerListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class UnshortenerListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = UnshortenerSerializer


class ShortenerCreateApiView(CreateAPIView):
    serializer_class = LinkSerializer


class UnshortenerCreateApiView(CreateAPIView):
    serializer_class = UnshortenerSerializer


class Redirector(View):
    def get(self, request, shortener_link, *args, **kwargs):
        shortener_link = settings.HOST_URL + '/' + self.kwargs['shortener_link']
        redirect_link = Link.objects.filter(shortened_link=shortener_link).first().original_link
        return redirect(redirect_link)
