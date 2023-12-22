from rest_framework import serializers
from .models import Slot
from customauth.models import User

#class ProfessionalSerializer(serializers.ModelSerializer):
#    image_url = serializers.ImageField(required=False)
#    
#    class Meta:
#        model = Professional
#        fields = '__all__'

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'

class ASlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        exclude = ['booked','flag']
