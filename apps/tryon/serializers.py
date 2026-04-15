from rest_framework import serializers
from .models import TryonRecord


class TryonRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TryonRecord
        fields = '__all__'