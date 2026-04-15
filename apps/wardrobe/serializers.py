from rest_framework import serializers
from .models import Clothing, ClothingCategory


class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = '__all__'


class ClothingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingCategory
        fields = '__all__'