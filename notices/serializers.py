from rest_framework import serializers
from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Notice
        fields = '__all__'