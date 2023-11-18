from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, SubserviceViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'subservices', SubserviceViewSet, basename='subservice')

urlpatterns = router.urls
