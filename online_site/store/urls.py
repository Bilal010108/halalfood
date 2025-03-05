from .views import *
from rest_framework import routers
from django.urls import path,include




router = routers.SimpleRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserProfileAPIView.as_view(), name='user'),
    path('user/<int:pk>/', UserProfileAPIView.as_view(), name='user'),

    path('category/', CategoryListAPIView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryListAPIView.as_view(), name='category'),

    path('categorytwo/', CategoryTwoListAPIView.as_view(), name='category_two'),
    path('categorytwo/<int:pk>/', CategoryTwoDetailAPIView.as_view(), name='category_two'),

    path('stor/', StoreListAPIView.as_view(), name='store_list'),
    path('stor/<int:pk>/', StoreDetailAPIView.as_view(), name='store_detail'),

    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),

    path('order/', OrderListAPIView.as_view(), name='order_list'),
    path('order/<int:pk>/', OrderDetailAPIView.as_view(), name='order_detail')

]