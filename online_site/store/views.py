from django.shortcuts import render
from rest_framework import viewsets, generics, status
from .serializers import *
from .models import *
# Create your views here.



class UserProfileAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers




class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryTwoAPIView(generics.ListAPIView):
    queryset = CategoryTwo.objects.all()
    serializer_class = CategoryTwoSerializers


class StoreAPIViewAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class OrderAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = CategoryTwoSerializers


class CartAPIViewAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = StoreSerializers


class CartItemAPIView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializers
