from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import SlotSerializer, ASlotSerializer
from .models import Slot
#from service.models import Subservice
#
#class ProfessionalViewSet(viewsets.ModelViewSet):
#    serializer_class = ProfessionalSerializer
#
#    def get_queryset(self):
#        subservice = self.request.GET.get('subservice')
#        queryset = Professional.objects.all()
#        if subservice is not None:
#            subservice = Subservice.objects.get(id=subservice)
#            queryset = subservice.professionals
#        return queryset

class FullSlotViewSet(viewsets.ModelViewSet):
    serializer_class = ASlotSerializer

    def get_queryset(self):
        booked_slots = Slot.objects.filter(booked=True)
        return booked_slots

class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
