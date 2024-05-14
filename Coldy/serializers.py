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