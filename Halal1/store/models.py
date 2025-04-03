from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django .contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True,blank=True, region='KG')
    ROLES_CHOICES = (
        ('клиент', 'клиент'),
        ('владелец', 'владелец'),
        ('курьер', 'курьер'),
    )
    user_role = models.CharField(max_length=16, choices=ROLES_CHOICES, default='клиент')

    def __str__(self):
        return self.username


class Category(models.Model):
    category_name = models.CharField(max_length=26,unique=True)
    category_image = models.ImageField(upload_to=' category_image/')

    def __str__(self):
        return f'{self.category_name}'





class CategoryTwo(models.Model):
    category_name=models.CharField(max_length=26,unique=True,)
    category_image = models.ImageField(upload_to='category_images/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='category_two')


    def __str__(self):
        return f'{self.category_name}'



class Product(models.Model):
    product_name = models.CharField(max_length=26)
    product_image=models.ImageField(upload_to='product_image/')
    category =models.ForeignKey(CategoryTwo,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    product_price = models.DecimalField(max_digits=7, decimal_places=2)
    stock =models.PositiveSmallIntegerField(default=1,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.category},{self.product_name}'


class Courier(models.Model):
    user = models.ForeignKey(UserProfile,related_name='user',on_delete=models.CASCADE)
    STATUS_COURIER_CHOICES = [

        ('доступен', 'доступен'),
        ('занят', 'занят')

    ]

    status_courier = models.CharField(max_length=20,choices=STATUS_COURIER_CHOICES,default='доступен')


    def __str__(self):
       return f'{self.user},{self.status_courier}'



class Cart(models.Model):
    client_cart = models.ForeignKey(UserProfile,related_name='client_cart',on_delete=models.CASCADE)


    def __str__(self):
       return f'{self.client_cart}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart', on_delete=models.CASCADE,)
    product_cart = models.ForeignKey(Product,related_name='product_cart',on_delete=models.CASCADE)
    quantity_cart =models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product_cart}'


class Order(models.Model):
    client = models.ForeignKey(UserProfile, related_name='product_owners', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='carts_orders', on_delete=models.CASCADE)
    STATUS_ORDER_CHOICES = [
        ('Ожидает обработки', 'Ожидает обработки'),
        ('В процессе доставки', 'В процессе доставки'),
        ('Доставлен', 'Доставлен'),
        ('Отменен', 'Отменен')
    ]
    status_order = models.CharField(max_length=20, choices=STATUS_ORDER_CHOICES, default='Ожидает обработки')
    delivery_address = models.TextField(null=True, blank=True)
    courier = models.ForeignKey(UserProfile, related_name='order_courier', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)


