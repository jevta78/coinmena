from rest_framework import serializers

from data.models import BtcUsd


class BtcUsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = BtcUsd
        fields = '__all__'
