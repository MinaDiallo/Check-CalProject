from rest_framework import serializers
from .models import*

class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['id', 'name', 'description', 'rate']
        
class CreateFoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['name', 'description', 'rate']