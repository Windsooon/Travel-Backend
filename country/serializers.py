from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = (
            'name', 'position', 'thumnails', 'create_time'
        )