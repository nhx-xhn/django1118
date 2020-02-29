from django import template
register=template.Library()

@register.filter()
def myadd(num1,num2):
    return num1+num2