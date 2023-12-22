from rest_framework.routers import DefaultRouter
from .views import SlotViewSet, FullSlotViewSet

router = DefaultRouter()
#router.register(r'professionals', ProfessionalViewSet, basename='professional')
router.register(r'testslots', SlotViewSet)
router.register(r'slots', FullSlotViewSet, basename='slot')

urlpatterns = router.urls
