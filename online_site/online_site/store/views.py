from django.shortcuts import render
from rest_framework import viewsets, generics, status
from .serializers import *
from .models import *




class UserProfileAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers




class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers


class CategoryTwoListAPIView(generics.ListAPIView):
    queryset = CategoryTwo.objects.all()
    serializer_class = CategoryTwoListSerializers


class CategoryTwoDetailAPIView(generics.RetrieveAPIView):
    queryset = CategoryTwo.objects.all()
    serializer_class = CategoryTwoDetailSerializers


class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializers


class StoreDetailAPIView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializers




class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializers


class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializers


class CartListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers


class CartItemListAPIView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers
