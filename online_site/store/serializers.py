from .admin import *
from rest_framework import serializers


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['last_name','first_name','phone_number','user_role','age']



class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['last_name','first_name']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['category_name']


class CategorySimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['category_name']

class CategoryTwoSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryTwo
        fields =['category_name']




class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'description',
                  'price', 'quantity', 'category','product_image']



class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields =['client','products',
                 'delivery_address','created_at',]



class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields =['client_cart']



class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        cart = models.ForeignKey(Cart, related_name='cart', on_delete=models.CASCADE, )
        fields =['cart','product_cart','quantity_cart']
