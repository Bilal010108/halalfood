from .views import *
from rest_framework import routers
from django.urls import path,include




router = routers.SimpleRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserProfileAPIView.as_view(), name='user'),
    path('user/<int:pk>/', UserProfileAPIView.as_view(), name='user'),



    path('category/', CategoryAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryAPIView.as_view(), name='category_detail'),

    path('categorytwo/', CategoryTwoAPIView.as_view(), name='category_two'),
    path('categorytwo/<int:pk>/', CategoryTwoAPIView.as_view(), name='category_two'),


    path('category/', CategoryAPIView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryAPIView.as_view(), name='category'),

    path('product/', ProductAPIView.as_view(), name='product'),
    path('product/<int:pk>/', ProductAPIView.as_view(), name='product'),

    path('order/', OrderAPIView.as_view(), name='order'),
    path('order/<int:pk>/', OrderAPIView.as_view(), name='order'),

    path('cart/', CartAPIView.as_view(), name='cart_list'),
    path('cart/<int:pk>/', CartAPIView.as_view(), name='cart_detail'),

    path('cartitem/', CartAPIView.as_view(), name='cartitem_list'),
    path('cartitem/<int:pk>/', CartAPIView.as_view(), name='cartitem_detail'),

]