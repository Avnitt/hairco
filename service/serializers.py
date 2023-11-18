from rest_framework import serializers
from .models import Service, Subservice

class SubserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subservice
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
