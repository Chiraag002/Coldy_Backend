from django.db import models

class LocationMaster(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=256)
    
    class Meta:
        db_table = "location_master"

class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=256)
    cust_no = models.CharField(max_length=256)
    shop_name = models.CharField(max_length=256)
    location_name = models.ForeignKey(LocationMaster,on_delete=models.CASCADE,
                    related_name='location_name',related_query_name="location_master"
                    ,null=True,blank=True)
    class Meta:
        db_table = 'customer'

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=256)
    product_desc = models.CharField(max_length=256)
    
    class Meta:
        db_table = 'product'

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(Customer,on_delete=models.CASCADE,
                    related_name='cust_id',related_query_name="customer"
                    ,null=True,blank=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,
                    related_name='product_id',related_query_name="product"
                    ,null=True,blank=True)
    product_qty = models.IntegerField(min_value=0) 
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=256)
    
    class Meta:
        db_table = 'orders' 