from django.http import JsonResponse,HttpResponse
import json
from product.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializers import *


# this was the basic function
# def api_home(request,*args, **kwargs):
#     #request ->http request ->django
#     #
#     return JsonResponse({"message":"Hi there,this your django api response!"})

# this is the improved one
# def api_home(request,*args, **kwargs):
#     #request ->http request ->django
#     #print(dir(request))
#     # request.body
#     print(request.GET)
#     print(request.POST)
#     body=request.body
#     data={}
#     try:
#         data=json.loads(body)
#     except:
#         pass
#     print(data)
#     data['params']=dict(request.GET)
#     data['headers']=dict(request.headers)
#     data['content_type']=request.content_type
#     return JsonResponse(data)


# using the model
# def api_home(request,*args, **kwargs):
#     model_data=Product.objects.all().order_by("?").first()
#     data={}
#     if model_data:
#         # data['id']=model_data.id
#         # data['title']=model_data.title
#         # data['content']=model_data.content
#         # data['price']=model_data.price
#         # data=model_to_dict(model_data)#to change the model to python dictionnary
#         data=model_to_dict(model_data,fields=['id','title'])#to precise the fields
#     return JsonResponse(data)

# using HttpResponse
# def api_home(request,*args, **kwargs):
#     model_data=Product.objects.all().order_by("?").first()
#     data={}
#     if model_data:
#         data=model_to_dict(model_data,fields=['id','title'])
#         json_data=json.dumps(data)
#     return HttpResponse(json_data,headers={"content-type":"application/json"})

# rest framework view and response:we chnange the view into rf response

# @api_view(["GET"])
# def api_home(request,*args, **kwargs):
#     model_data=Product.objects.all().order_by("?").first()
#     data={}
#     if model_data:
#         data=model_to_dict(model_data,fields=['id','title','sale_price'])
#     return Response(data)

# using serializers
@api_view(["GET"])
def api_home(request,*args, **kwargs):
    instance=Product.objects.all().order_by("?").first()
    data={}
    if instance:
        # data=model_to_dict(instance,fields=['id','title','sale_price'])
        data=ProductSerializer(instance).data
    return Response(data)

# using POST method
@api_view(["POST"])
def api_home(request,*args, **kwargs):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        print(serializer.data)
        data=serializer.data
        return Response(data)
    return Response({"invalid":"not good data"},status=400)