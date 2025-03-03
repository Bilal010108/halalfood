from django.db import models
from django .contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    ROLES_CHOICES = (
        ('клиент', 'клиент'),
        ('владелец', 'владелец')
    )
    user_role = models.CharField(max_length=16, choices=ROLES_CHOICES, default='клиент')
    age = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(16), MaxValueValidator(50)])

    def __str__(self):
        return f'{self.user_role},{self.username}'



class Category(models.Model):
    category_name =models.CharField(max_length=20,unique=True)


    def __str__(self):
       return f'{self.category_name}'


class CategoryTwo(models.Model):
    category_name =models.CharField(max_length=20,unique=True)

    def __str__(self):
       return f'{self.category_name}'



class Store(models.Model):
    store_name = models.CharField(max_length=20)
    store_description =models.TextField(null=True,blank=True)
    contact_info = PhoneNumberField(null=True,blank=True,region='KG')
    address = models.TextField(null=True,blank=True)
    owner = models.ForeignKey(UserProfile,related_name='store',on_delete=models.CASCADE)
    store_image = models.ImageField(upload_to='store_image/', null=True, blank=True)


    def __str__(self):
        return f'{self.store_name}'



class Product(models.Model):
    product_name =models.CharField(max_length=16)
    description = models.TextField(null=True,blank=True)
    price = models.PositiveIntegerField(default=0)
    quantity =models.PositiveSmallIntegerField(default=1)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_product')
    category =models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category_product')
    product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)


    def __str__(self):
        return f'{self.product_name}'


class Order(models.Model):
    client =models.ForeignKey(UserProfile,related_name='product_owners',on_delete=models.CASCADE)
    products = models.ForeignKey(Product,related_name='products_orders',on_delete=models.CASCADE)
    delivery_address =models.TextField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client},{self.products}'

class Cart(models.Model):
    client_cart = models.ForeignKey(UserProfile,related_name='client_cart',on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.client_cart}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart', on_delete=models.CASCADE,)
    product_cart = models.ForeignKey(Product,related_name='product_cart',on_delete=models.CASCADE)
    quantity_cart =models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.cart},{self.product_cart}'