from rest_framework.routers import DefaultRouter
from product.viewsets import *

router=DefaultRouter()

router.register('product',ProductViewSet,basename='product')
# router.register('product',ProductGenericViewSet,basename='products')
urlpatterns = router.urls

