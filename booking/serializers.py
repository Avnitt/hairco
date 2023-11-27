from rest_framework import serializers
from .models import Appointment 
from service.serializers import AddonSerializer
from staff.serializers import SlotSerializer
from staff.models import Slot

class AppointmentSerializer(serializers.ModelSerializer):
    slot = SlotSerializer()
    class Meta:
        model = Appointment
        fields = '__all__'

    def create(self, validated_data):
        slot = validated_data['slot']
        slot['professional'] = validated_data['professional']
        slot = Slot.objects.create(**slot)
        validated_data['slot'] = slot
        addons = validated_data.pop('addons')
        appointment = Appointment.objects.create(**validated_data)
        for addon in addons:
            appointment.addons.add(addon)
        return appointment
