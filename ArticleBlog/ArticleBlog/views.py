from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.shortcuts import render
def index(request):
    return render(request,"index.html")

def gbook(request):
    return render(request,'gbook.html')

def about(request):
    return render(request,"about.html")

def list(request):
    return render(request,"list.html")

def info(request):
    return render(request,'info.html')

def base(request):
    return render(request,'base.html')

# def listpic(request):
#     return render(request,'listpic.html')

# def newlistpic(request):
#     return render(request,'newslistpic.html')
