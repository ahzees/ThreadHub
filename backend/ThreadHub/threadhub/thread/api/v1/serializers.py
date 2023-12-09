from rest_framework import serializers

from thread import models
from authentication.api.v1.serializers import CustomUserSerializer

class ThreadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Thread
        fields = ['pk', 'name']
        read_only_fields = ['pk',]

    def create(self, validated_data):
        return models.Thread.objects.create(**validated_data)
    

