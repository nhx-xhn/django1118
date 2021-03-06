"""DjangoLogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from LoginUser.views import *
from django.views.decorators.csrf import csrf_exempt
from LoginUser.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('base/', base),
    # path('index/', index),
    re_path('^$',index),
    path('loginuser/',include('LoginUser.urls')),
    # path('goodsview/',GoodsView.as_view()),
    path('goodsview/',csrf_exempt(GoodsView.as_view())),
]

urlpatterns +=router.urls


