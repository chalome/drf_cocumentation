from .models import *
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    the_discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product
        fields=[
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'the_discount'
        ]
    def get_the_discount(self,obj):
        try:
            return obj.get_discount()
        except:
            return None