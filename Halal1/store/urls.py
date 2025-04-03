from .views import *
from rest_framework import routers
from django.urls import path,include


router = routers.SimpleRouter()


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('', include(router.urls)),
    path('product/', ProductListAPIView.as_view(), name='product'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('product/create', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/create/<int:pk>/', ProductEDITAPIView.as_view(), name='product_edit'),


    path('user/', UserProfileAPIView.as_view(), name='user'),
    path('user/<int:pk>/', UserProfileAPIView.as_view(), name='user_detail'),


    path('category/', CategoryListAPIView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('category/<int:pk>/products/', ProductListAPIView.as_view(), name='category_products'),


    path('two/', CategoryTwoListAPIView.as_view(), name='category_two_list'),
    path('two/<int:pk>/', CategoryTwoDetailAPIView.as_view(), name='category_two_detail'),


    path('courier/', CourierAPIView.as_view(), name='courier'),
    path('courier/<int:pk>/', CourierAPIView.as_view(), name='courier_detail'),


    path('cart/', CartAPIView.as_view(), name='cart_list'),


    path('cartitem/', CartItemAPIView.as_view(), name='cartitem_list'),
    path('cartitem/<int:pk>/', CartItemAPIView.as_view(), name='cartitem_detail'),

]

