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
