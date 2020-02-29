##便携过滤器
#1导包
from django import template
#2实例化对象
register = template.Library()





##前段调用
@register.filter()
def myadd(num):
    return num+num
@register.filter()
def my_two_add(num1,num2):
    return num1+num2


