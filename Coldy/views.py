from .serializers import *
from rest_framework import filters 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView , ListAPIView , RetrieveAPIView


class LocationApiView(ListCreateAPIView):
    queryset = LocationMaster.objects.all()
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    search_fields = ['location_name']
    ordering_fields = ['location_name'] 
    ordering = ['location_name']
    serializer_class = LocationMasterSerializer 
    
class UpdateLocationApiView(RetrieveUpdateDestroyAPIView):
    queryset = LocationMaster.objects.all()
    search_fields = ['location_name']
    ordering_fields = ['location_name'] 
    ordering = ['location_name']
    serializer_class = LocationMasterSerializer    
    
class CustomerApiView(ListCreateAPIView):
    queryset = Customer.objects.all()
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    search_fields = ['cust_name']
    ordering_fields = ['cust_name'] 
    ordering = ['cust_name']
    serializer_class = CustomerMasterSerializer 
    
class UpdateCustomerApiView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    search_fields = ['cust_name']
    ordering_fields = ['cust_name'] 
    ordering = ['cust_name']
    serializer_class = CustomerMasterSerializer    
    
class ProductApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    search_fields = ['product_name']
    ordering_fields = ['product_name'] 
    ordering = ['product_name']
    serializer_class = ProductMasterSerializer 
    
class UpdateProductApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    search_fields = ['product_name']
    ordering_fields = ['product_name'] 
    ordering = ['product_name']
    serializer_class = ProductMasterSerializer    
    
class OrdersApiView(ListCreateAPIView):
    queryset = Orders.objects.all()
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    search_fields = ['product__product_name']
    ordering_fields = ['product__product_name'] 
    ordering = ['product__product_name']
    serializer_class = OrdersMasterSerializer 
    
class UpdateOrdersApiView(RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    search_fields = ['product__product_name']
    ordering_fields = ['product__product_name'] 
    ordering = ['product__product_name']
    serializer_class = OrdersMasterSerializer    
