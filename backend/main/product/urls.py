from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/',product_detail_view),
    path('create/',product_create_view),
    path('',product_list_view),
    path('create_list/',product_create_list_view),
    path('create_list_/',product_alt_view),
    path('update/<int:pk>/',product_update_view),
    path('delete/<int:pk>/',product_delete_view),
]
