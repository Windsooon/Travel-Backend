from rest_framework import serializers
from .models import App


class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = App
        fields = (
            'name', 'company', 'description',
            'category', 'thumnails', 'des_thumnails',
            'language', 'rating', 'store_url', 'create_time'
        )
