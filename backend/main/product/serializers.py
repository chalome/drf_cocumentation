from .models import *
from rest_framework import serializers
from rest_framework.reverse  import reverse
from .validators import *
from api.serializers import UserPublicSerializer

class ProductInlineSerializer(serializers.Serializer):
    url=serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk',read_only=True)
    title=serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    # user=UserPublicSerializer(read_only=True)
    owner=UserPublicSerializer(source='user',read_only=True)
    # related_products=ProductInlineSerializer(source='user.product_set.all',many=True,read_only=True)
    # my_user_data=serializers.SerializerMethodField(read_only=True)
    the_discount=serializers.SerializerMethodField(read_only=True)
    edit_url=serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk')
    email=serializers.EmailField(write_only=True)
    # email=serializers.EmailField(source='user.email',read_only=True)
    title=serializers.CharField(validators=[unique_product_title_validator,validate_title_no_number])
    body=serializers.CharField(source='content')
    class Meta:
        model=Product
        fields=[
            'pk',
            # 'user',
            'owner',
            # 'related_products',
            'url',
            'edit_url',
            'email',
            'title',
            'body',
            'price',
            'sale_price',
            'the_discount',
            # 'my_user_data',
            'public',
        ]
    def get_my_user_data(self,obj):
        return{
            "username":obj.user.username
        }
    # def get_url(self,obj):
    #     # return f'/api/products/{obj.pk}/'
    #     request=self.context.get('request')
    #     if request is None:
    #         return None
    #     # reverse(request,'product-detail',kwargs={'pk':obj.pk})
    #     return reverse("product-edit",kwargs={"pk":obj.pk},request=request)
    def get_edit_url(self,obj):
        request=self.context.get('request')
        if request is None:
            return None
        # reverse(request,'product-detail',kwargs={'pk':obj.pk})
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request)
    def get_the_discount(self,obj):
        try:
            return obj.get_discount()
        except:
            return None
    
    def create(self,validated_data):
        # email=validated_data.pop('email')
        # object= Product.objects.create(**validated_data)
        object= super().create(validated_data)
        # print(email,object)
        return object
    
    def update(self, instance, validated_data):
        validated_data.pop('email')
        return super().update(instance, validated_data)
    
    
    #           i moved this to validators.py            #
    
    # def validate_title(self,value):
    #     qs=Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError("This title already exists")
    #     return value
    
    # it can be neccessary to declare it here for the request
    
    # def validate_title(self,value):
    #     request=self.context.get('request')
    #     user=request.user
    #     qs=Product.objects.filter(user=user,title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError("This title already exists")
    #     return value
    
    # per user validation
    
    # def validate_title_for_user(self,value):
    #         request=self.context.get('request')
    #         user=request.user
    #         qs=Product.objects.filter(user=user,title__iexact=value)
    #         if qs.exists():
    #             raise serializers.ValidationError("This title already exists")
    #         return value