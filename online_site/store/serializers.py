from .admin import *
from rest_framework import serializers


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'last_name','first_name','phone_number','user_role','age']


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['last_name','first_name']



class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id', 'category_name']

class CategoryDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['category_name']

class CategorySimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['category_name',]


class CategoryTwoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryTwo
        fields =['id', 'category_name']


class CategoryTwoDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryTwo
        fields =['category_name']


class StoreListSerializers(serializers.ModelSerializer):
    category_st =CategorySimpleSerializers(read_only=True)
    class Meta:
        model = Store
        fields =['id', 'category_st','store_name',
                 'contact_info','store_image']


class StoreDetailSerializers(serializers.ModelSerializer):
    owner = UserProfileSimpleSerializers()
    category_st =CategorySimpleSerializers(read_only=True)
    class Meta:
        model = Store
        fields =['id', 'category_st','store_name','store_description',
                 'contact_info','address','owner','store_image']



class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'quantity', 'product_image']



class ProductDetailSerializers(serializers.ModelSerializer):
    store = StoreListSerializers(read_only=True)
    category = CategoryListSerializers(read_only=True)
    class Meta:
        model = Product
        fields = ['product_name', 'description',
                  'price', 'quantity', 'store', 'category','product_image']


class OrderListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields =['client','products',
                 'delivery_address','created_at',]


class OrderDetailSerializers(serializers.ModelSerializer):
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
