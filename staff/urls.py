from rest_framework.routers import DefaultRouter
from .views import ASlotViewSet

router = DefaultRouter()
#router.register(r'professionals', ProfessionalViewSet, basename='professional')
router.register(r'slots', ASlotViewSet, basename='slot')

urlpatterns = router.urls
