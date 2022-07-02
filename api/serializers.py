from rest_framework import serializers

from . import models

class BitcoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bitcoin
        fields = ('symbol', 'price', 'timestamp')