from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register('manufacturer', ManufacturerViewSet)
router.register('product', ProductViewSet)

urlpatterns = router.get_urls()

