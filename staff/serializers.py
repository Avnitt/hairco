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
    def validate(self, attrs):
        start_time = attrs.get('start_time')
        bookings = Slot.objects.filter(start_time=start_time)
        if len(bookings) == 3:
            self.booked = True

        return attrs

    class Meta:
        model = Slot
        exclude = ['booked']
