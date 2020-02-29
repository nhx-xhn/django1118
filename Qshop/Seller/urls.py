from django.urls import path,re_path
from .views import *

urlpatterns=[
    path('login/',login),
    path('logout/',logout),
    path('register/',register),
    path('index/',index),
    path('base/',base),
    path('goods_add/',goods_add),
    # path('add_label/',add_label),
    path('user_profile/',user_profile),
    re_path('goods_list/(?P<page>\d+)/(?P<status>\d+)/',goods_list),
    re_path('goods_status/(?P<id>\d+)/(?P<status>\w+)/', goods_status),

]





