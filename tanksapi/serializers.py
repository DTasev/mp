from rest_framework import serializers
from tanksapi.models import Map
from django.db import transaction
from django.utils import timezone


class ListMapSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="tanksapi:map-detail")

    class Meta:
        model = Map
        fields = ('id', 'url', 'thumbnail_url', 'name', 'creator', 'created')


class MapCreatorSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="tanksapi:map-detail")

    class Meta:
        model = Map
        fields = ('id', 'url', 'thumbnail_url', 'name', 'creator', 'terrain')

    def create(self, validated_data):
        with transaction.atomic():
            created = timezone.now()
            user = None
            request = self.context.get("request")
            if request and hasattr(request, "user"):
                user = request.user
            validated_data["created"] = created
            validated_data["creator"] = user
            return Map.objects.create(**validated_data)


class SingleMapSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="tanksapi:map-detail")

    class Meta:
        model = Map
        fields = ('id', 'url', 'thumbnail_url', 'name', 'creator', 'created', 'terrain')
