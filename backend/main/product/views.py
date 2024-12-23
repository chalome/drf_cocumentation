from rest_framework import generics,permissions,authentication
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .permissions import IsStaffEditorPersmission
from api.authentication import TokenAuthentication


class ProductDetailView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        # print(serializer)
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content)
        
class ProductListView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class ProductCreateListView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # authentication_classes=[authentication.SessionAuthentication,authentication.TokenAuthentication]
    authentication_classes=[authentication.SessionAuthentication,TokenAuthentication]#custom Bearer token
    # permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    # permission_classes=[permissions.DjangoModelPermissions]
    # permission_classes=[IsStaffEditorPersmission]
    permission_classes=[permissions.IsAdminUser, IsStaffEditorPersmission]
    

class ProductUpdateView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductDeleteView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
product_create_view=ProductCreateView.as_view()
product_update_view=ProductUpdateView.as_view()
product_delete_view=ProductDeleteView.as_view()
product_detail_view=ProductDetailView.as_view()
product_list_view=ProductListView.as_view()
product_create_list_view=ProductCreateListView.as_view()

@api_view(["get","post"])
def product_alt_view(request,pk=None,*args, **kwargs):
    method=request.method
    if method=="GET":
        if pk is not None:
            #detail view
            obj=get_object_or_404(Product,pk=pk)
            data=ProductSerializer(obj,many=False).data
            return Response(data)
        queryset=Product.objects.all()
        data=ProductSerializer(queryset,many=True).data
        return Response(data)
    
    if method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content') or None
            if content is None:
                content=title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid":"not good data"},status=400)
    
# mixins :class based views

