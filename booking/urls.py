from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet

router = DefaultRouter()
router.register(r'book', AppointmentViewSet, basename='book')

urlpatterns = router.urls
