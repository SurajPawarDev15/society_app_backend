from rest_framework import serializers
from .models import Visitor

class VisitorSerializer(serializers.ModelSerializer):
    resident = serializers.ReadOnlyField(source='resident.username')

    class Meta:
        model = Visitor
        fields = '__all__'