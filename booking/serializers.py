from rest_framework import serializers
from .models import Appointment
from staff.serializers import ASlotSerializer
from staff.models import Slot
from service.serializers import AddonSerializer, SubserviceSerializer
from service.models import Addon
from django.core.exceptions import ObjectDoesNotExist


class AppointmentSerializer(serializers.ModelSerializer):
    slot = ASlotSerializer()
    addons = serializers.PrimaryKeyRelatedField(queryset=Addon.objects.all(),
                                                many=True,
                                                required=False)

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

        except ObjectDoesNotExist:
            slot = Slot.objects.create(**slot)
        validated_data['slot'] = slot
        addons = validated_data.pop('addons', [])
        appointment = Appointment.objects.create(**validated_data)
        for addon in addons:
            appointment.addons.add(addon)
        return appointment


class UserAppointmentSerializer(serializers.ModelSerializer):
    slot = ASlotSerializer()
    addons = AddonSerializer(many=True)
    subservice = SubserviceSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'
