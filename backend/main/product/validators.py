from .models import *
from rest_framework import serializers
from .serializers import *
from rest_framework import validators

def validate_title(value):
        qs=Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("This title already exists")
        return value

def validate_title_no_number(value):
    if any(char.isdigit() for char in value):
        raise serializers.ValidationError("This title cannot contain numbers")
    return value

unique_product_title_validator=validators.UniqueValidator(queryset=Product.objects.all())