"""
URL configuration for Coldy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_location/', LocationApiView.as_view(),name="LocationApiView"),  
    path('update_location/<int:pk>', UpdateLocationApiView.as_view(),name="UpdateLocationApiView"),  
    path('add_customer/', CustomerApiView.as_view(),name="customerApiView"),  
    path('update_customer/<int:pk>', UpdateCustomerApiView.as_view(),name="UpdatecustomerApiView"),  
    path('add_product/', ProductApiView.as_view(),name="ProductApiView"),  
    path('update_product/<int:pk>', UpdateProductApiView.as_view(),name="UpdateProductApiView"),  
    path('add_Orders/', OrdersApiView.as_view(),name="OrdersApiView"),  
    path('update_Orders/<int:pk>', UpdateOrdersApiView.as_view(),name="UpdateOrdersApiView"),  
]
