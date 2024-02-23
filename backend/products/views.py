from django.shortcuts import render

# Create your views here.
from rest_framework import generics,permissions
from  .models import Product
from .serializers import ProductSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer