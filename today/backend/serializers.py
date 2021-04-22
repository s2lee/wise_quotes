from rest_framework import serializers
from .models import WiseQuotes

class WiseQuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WiseQuotes
        fields = '__all__'