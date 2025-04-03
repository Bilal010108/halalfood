from .models import *
from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields =['phone_number','user_role','first_name','last_name','username']


class CategorySimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ['category_name']


class CategoryTwoSimplesSerializers(serializers.ModelSerializer):
    class Meta:
        model=CategoryTwo
        fields = ['category_name','category_image']


class CategoryTwoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryTwo
        fields = ['category_name','category_image']



class CategoryTwoDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryTwo
        fields = '__all__'



class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_image']


class CategoryDetailSerializers(serializers.ModelSerializer):
    category_two =CategoryTwoSimplesSerializers(read_only=True, many=True)
    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializers(serializers.ModelSerializer):
    category =CategorySimpleSerializers(read_only=True)
    class Meta:
        model =Product
        fields = ['id','product_name','product_image',
                  'product_price','category']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializers(serializers.ModelSerializer):
    category =CategorySimpleSerializers(read_only=True)
    class Meta:
        model =Product
        fields = ['id','product_name','product_image','category','quantity',
                  'description','product_price','stock',
                                'created_at','updated_at']



class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields = ['client_cart']


class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields = ['cart','product_cart','quantity_cart']


class CourierSerializers(serializers.ModelSerializer):
    class Meta:
        model=Courier
        fields = ['user','status_courier']

