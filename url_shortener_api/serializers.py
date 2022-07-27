from rest_framework.serializers import ModelSerializer
from .models import Link, UnshortenerLink


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


class UnshortenerSerializer(ModelSerializer):
    class Meta:
        model = UnshortenerLink
        fields = '__all__'
