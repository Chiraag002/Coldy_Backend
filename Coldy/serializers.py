from rest_framework import serializers
from .models import *


# Add serializer  below here 
class LocationMasterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LocationMaster  
        exclude= []


    def to_representation(self, instance:LocationMaster):
        return super().to_representation(instance)
    
    def validate(self, attrs):
        return super().validate(attrs) 

class CustomerMasterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer  
        exclude= []


    def to_representation(self, instance:LocationMaster):
        return super().to_representation(instance)
    
    def validate(self, attrs):
        return super().validate(attrs) 


class ProductMasterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product  
        exclude= []


    def to_representation(self, instance:LocationMaster):
        return super().to_representation(instance)
    
    def validate(self, attrs):
        return super().validate(attrs) 

class OrdersMasterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Orders  
        exclude= []


    def to_representation(self, instance:LocationMaster):
        return super().to_representation(instance)
    
    def validate(self, attrs):
        return super().validate(attrs) 
