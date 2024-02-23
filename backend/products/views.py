from django.shortcuts import render

# Create your views here.
from rest_framework import generics,permissions
from  .models import Product
from .serializers import ProductSerializer
from .permissions import IsAuthorOrReadOnly

class ProductList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer