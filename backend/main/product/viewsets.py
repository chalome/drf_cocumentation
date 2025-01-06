from rest_framework import viewsets,mixins
from .models import *
from .serializers import *

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductGenericViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


product_list_view=ProductGenericViewSet.as_view({'get':'list'})
product_detail_view=ProductGenericViewSet.as_view({'get':'retrieve'})