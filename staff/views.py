from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import ProfessionalSerializer, SlotSerializer
from .models import Professional, Slot
from service.models import Subservice

class ProfessionalViewSet(viewsets.ModelViewSet):
    serializer_class = ProfessionalSerializer

    def get_queryset(self):
        subservice = self.request.GET.get('subservice')
        queryset = Professional.objects.all()
        if subservice is not None:
            subservice = Subservice.objects.get(id=subservice)
            queryset = subservice.professionals
        return queryset

class ASlotViewSet(viewsets.ModelViewSet):
    serializer_class = SlotSerializer
    
    def get_queryset(self):
        professional = self.request.GET.get('professional')
        if professional is None:
            return Slot.objects.all()
        available_slots = Slot.objects.filter(professional=professional, booked=True)
        return available_slots
