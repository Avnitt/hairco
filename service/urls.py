from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, SubserviceViewSet, AddonViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'subservices', SubserviceViewSet, basename='subservice')
router.register(r'addons', AddonViewSet)

urlpatterns = router.urls
