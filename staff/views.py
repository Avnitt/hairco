from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import SlotSerializer
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
 
class ASlotViewSet(viewsets.ModelViewSet):
    serializer_class = SlotSerializer
    
    def get_queryset(self):
        booked_slots = Slot.objects.filter(booked=True)
        return booked_slots
