from rest_framework import serializers

from core.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'api_key', 'created', 'updated')
        extra_kwargs = {
            'api_key': {'read_only': True}
        }
