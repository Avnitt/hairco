from django.shortcuts import render
from .serializers import ServiceSerializer, SubserviceSerializer, AddonSerializer
from .models import Service, Subservice, Addon
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

#    def get_permissions(self):
#        if self.action == 'list':
#            permission_classes = [AllowAny]
#        else:
#            permission_classes = [IsAdminUser]
#        return [permission() for permission in permission_classes]

class SubserviceViewSet(viewsets.ModelViewSet):
    serializer_class = SubserviceSerializer

    def get_queryset(self):
        service = self.request.GET.get('service')
        if service is None:
            queryset = Subservice.objects.all()
        else:
            queryset = Subservice.objects.filter(service=service)
        return queryset

class AddonViewSet(viewsets.ModelViewSet):
    queryset = Addon.objects.all()
    serializer_class = AddonSerializer
