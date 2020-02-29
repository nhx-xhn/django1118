"""Demo URL Configuration

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

from django.urls import path,re_path
from .views import *
# from django.contrib import admin
urlpatterns = [
    # path('admin/',admin.site.urls),
    path('index/',index),
    path('about/',about),
    path('listpic/',listpic),
    # re_path('newslistpic/',newslistpic),
    re_path('newslistpic/(?P<page>\d+)/',newslistpic),
    re_path('articleinfo/(?P<id>\d*)/',articleinfo),
    path('base/',base),
    path('choices_text/',choices_text),
    path('add_app01/',add_app01),
    path('fy_test/',fy_test),
    path('request_demo/',request_demo),
    # path('get_test/',get_test),
    # path('post_demo/',post_demo),
    path('getdemo/',getdemo),
    path('qqtest/',qqtest),
    path('qqtest/',qqtest),
    path('register/',register),
    path('zhuce/',zhuce),
    path('ajaxdemo/',ajaxdemo),
    path('ajax_register/',ajax_register),
    path('ajax_get_req/',ajax_get_req),
    path('ajax_post_req/',ajax_post_req),
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('delete_cookie/',delete_cookie),
    path('set_session/',set_session),
    path('get_session/',get_session),
    path('delete_session/',delete_session),



]



