from django.urls import path
from .views import *
urlpatterns = [
    path('adduser/',adduser),
    path('getuser/',getuser),
    path('update_user/',update_user),
    path('delete_user/',delete_user),
    path('mohu_user/',mohu_user),
    path('add_f/',add_f),
    path('get_f/',get_f),
    path('update_f/',update_f),
    path('delete_f/',delete_f),
    path('add_many/',add_many),
    path('get_many/',get_many),
    path('update_many/',update_many),
    path('delete_many/',delete_many),
    path('juhe/',juhe),
    path('tiaojian/',tiaojian)

]


