from django.db import models
from django.conf import settings
from django.db.models import Q

user=settings.AUTH_USER_MODEL

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self,query,user=None):
        lookup=Q(title__icontains=query) | Q(content__icontains=query)
        qs=self.is_public().filter(lookup)
        if user is not None:
            qs2=qs.filter(user=user).filter(lookup)
            qs=(qs | qs2).distinct()
        return qs

class ProductManager(models.Manager):
    def get_queryset(self,*args, **kwargs):
        return ProductQuerySet(self.model,using=self._db)

# class ProductManager(models.Manager):
#     def search(self,query,user=None):
#         return Product.objects.first(public=True).filter(title__icontains=query)

# class ProductManager(models.Manager):
#     def search(self,query,user=None):
#         return Product.objects.first(public=True).filter(title__icontains=query)

class Product(models.Model):
    user=models.ForeignKey(user,on_delete=models.SET_NULL,null=True,default=1)
    title=models.CharField(max_length=129)
    content=models.TextField(blank=True,null=True)
    price =models.DecimalField(max_digits=15,decimal_places=2,default=99.99)
    public=models.BooleanField(default=True)
    
    objects=ProductManager()
    
    def __str__(self):
        return self.title

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)
    
    def get_discount(self):
        return "122"