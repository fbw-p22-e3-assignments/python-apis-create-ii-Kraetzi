from django.shortcuts import render

# Create your views here.

from .models import Product #new
from rest_framework import generics #new
from rest_framework.permissions import IsAuthenticated  # new
from .serializers import ProductSerializer #new

# new token can be created for the super user of the project 
#user = dci
#password = dci12345
# Run "python manage.py drf_create_token dci" in terminal to generate a fresh token

class ProductList(generics.ListAPIView):
    # API endpoint that allows product to be viewed.
    permission_classes = [IsAuthenticated]  
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new product
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all(),
    serializer_class = ProductSerializer

class ProductDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a product record to be deleted.
    permission_classes = [IsAuthenticated] 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single product by id.
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer