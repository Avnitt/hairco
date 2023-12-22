from rest_framework import serializers
from .models import Appointment 
from service.serializers import AddonSerializer
from staff.serializers import ASlotSerializer
from staff.models import Slot
from customauth.models import User

class AppointmentSerializer(serializers.ModelSerializer):
    slot = ASlotSerializer()
    class Meta:
        model = Appointment
        fields = '__all__'

    def create(self, validated_data):
        slot = validated_data['slot']
        try:
            slot = Slot.objects.get(start_time=slot['start_time'])
            slot.flag = slot.flag + 1
            if slot.flag == 3:
                slot.booked = True
            slot.save()

        except:
            slot = Slot.objects.create(**slot)
        validated_data['slot'] = slot
        addons = validated_data.pop('addons')
        appointment = Appointment.objects.create(**validated_data)
        for addon in addons:
            appointment.addons.add(addon)
        return appointment

class UserAppointmentSerializer(serializers.ModelSerializer):
    slot = ASlotSerializer()
    class Meta:
        model = Appointment
        fields = '__all__'
