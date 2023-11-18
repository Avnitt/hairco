from django.shortcuts import render
from .serializers import ServiceSerializer, SubserviceSerializer
from .models import Service, Subservice
from rest_framework import viewsets

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class SubserviceViewSet(viewsets.ModelViewSet):
    serializer_class = SubserviceSerializer

    def get_queryset(self):
        service = self.request.GET.get('service')
        if service is None:
            queryset = Subservice.objects.all()
        else:
            queryset = Subservice.objects.filter(service=service)
        return queryset
