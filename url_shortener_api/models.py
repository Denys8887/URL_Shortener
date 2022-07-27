import http.client
import urllib.parse
from random import choices
from string import ascii_letters

from django.conf import settings
from django.db import models


class Link(models.Model):
    original_link = models.URLField()
    shortened_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def shortener(self):
        while True:
            random_string = "".join(choices(ascii_letters, k=6))
            new_link = settings.HOST_URL + "/" + random_string

            if not Link.objects.filter(shortened_link=new_link).exists():
                break

        return new_link

    def save(self, *args, **kwargs):
        if not self.shortened_link:
            new_link = self.shortener()
            self.shortened_link = new_link
        return super().save(*args, **kwargs)


class UnshortenerLink(models.Model):
    shortened_link = models.URLField()
    original_link = models.URLField(blank=True, null=True)

    def unshortener_url(self):
        parsed = urllib.parse.urlparse(self)
        h = http.client.HTTPConnection(parsed.netloc)
        h.request("HEAD", parsed.path)
        response = h.getresponse()
        if response.status / 100 == 3 and response.getheader("Location"):
            return response.getheader("Location")
        else:
            return self

    def save(self, *args, **kwargs):
        if not self.shortened_link:
            new_link = self.original_link
            self.original_link = new_link
        return super().save(*args, **kwargs)
