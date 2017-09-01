from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = (
            'name', 'position', 'thumbnail', 'create_time'
        )
