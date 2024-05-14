from .abstract_model import *
from .models_manager import *
from django.db import models



class LocationMaster(CommonFields):  
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=256)
    
    class Meta:
        db_table = "location_master"
        
    objects = ModelManager 
    Allobjects = AllModelManager 

class Customer(CommonFields):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=256)
    cust_no = models.CharField(max_length=256)
    shop_name = models.CharField(max_length=256)
    location = models.ForeignKey(LocationMaster,on_delete=models.CASCADE,
                    related_name='location_nm',related_query_name="location_nms"
                    ,null=True,blank=True)
    class Meta:
        db_table = 'customer'

    objects = ModelManager 
    Allobjects = AllModelManager

class Product(CommonFields):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=256)
    product_desc = models.CharField(max_length=256)
    
    class Meta:
        db_table = 'product'

    objects = ModelManager 
    Allobjects = AllModelManager

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,
                    related_name='customer',related_query_name="customers"
                    ,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,
                    related_name='product',related_query_name="products"
                    ,null=True,blank=True)
    product_qty = models.IntegerField() 
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=256)
    
    class Meta:
        db_table = 'orders' 