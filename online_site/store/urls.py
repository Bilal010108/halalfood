from .views import *
from rest_framework import routers
from django.urls import path,include




router = routers.SimpleRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserProfileAPIView.as_view(), name='user'),
    path('user/<int:pk>/', UserProfileAPIView.as_view(), name='user'),

    path('category/', CategoryAPIView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryAPIView.as_view(), name='category'),

    path('categorytwo/', CategoryTwoAPIView.as_view(), name='category_two'),
    path('categorytwo/<int:pk>/', CategoryTwoAPIView.as_view(), name='category_two'),

    path('stor/', StoreAPIViewAPIView.as_view(), name='user'),
    path('stor/<int:pk>/', StoreAPIViewAPIView.as_view(), name='user'),

    path('category/', CategoryAPIView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryAPIView.as_view(), name='category'),

]