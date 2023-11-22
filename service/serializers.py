from rest_framework import serializers
from .models import Service, Subservice, Addon

class SubserviceSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    class Meta:
        model = Subservice
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    class Meta:
        model = Service
        fields = '__all__'

class AddonSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    class Meta:
        model = Addon
        fields = '__all__'
