
from django.urls import path,include
from .views import *

urlpatterns = [

    path('index/',index),
    path('login/',login),
    path('logout/',logout),
    path('register/',register),
    path('cart/',cart),
    path('add_cart/',add_cart),
    path('detail/',detail),
    path('list/',list),
    path('place_order/',place_order),
    path('goods_test/',goods_test),
    path('change_cart/',change_cart),
    path('cart_place_order/',cart_place_order),
    path('alipay_order/',alipay_order),
    path('pay_result/',pay_result),
    path('user_center_info/',user_center_info),
    path('user_center_order/',user_center_order),
    path('user_center_site/',user_center_site),
]