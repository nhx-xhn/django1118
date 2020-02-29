from django.shortcuts import render,render_to_response
from django.http import HttpResponse
# Create your views here.

##装饰器
def loginValid(func):
    def inner(request,*args,**kwargs):
        ##校验用户身份
        cookie_username=request.COOKIES.get('username')
        session_username=request.session.get('username')
        if cookie_username and session_username and cookie_username==session_username:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/login/')
    return inner


def base(request):
    return render(request,'base.html')

@loginValid
def index(request):
    ##返回数据
    ##1 返回6条文章数据   排序  安照时间逆序
    ##判断校验登录
    # cookie_username=request.COOKIES.get('username')
    # session_username=request.session.get('username')
    # if cookie_username and session_username and cookie_username==session_username:
        article=Article.objects.order_by('-date')[:6]
        # one=article[0]
        # print(one)
        # print(one.author)
        # print(one.type.first())
        ##2 返回图文推荐内容7条
        recommend_article=Article.objects.filter(recommend=1).order_by('-date')[:7]
        ##3  点击率排行12条
        ##有点击率      安点击率排逆序
        cilck_article=Article.objects.order_by('-cilck')[:12]
        return render(request,"index.html",locals())
    # else:
    #     return HttpResponseRedirect('/login/')

@loginValid
def about(request):
    return render(request,'about.html')


def articleinfo(request,id):
    ##查询指定文章详情  id
    # id=1
    article=Article.objects.get(id=id)
    article.cilck=article.cilck+1
    article.save()





    return render_to_response("articleinfo.html",locals())

def listpic(request):
    return render(request,'listpic.html')

def newslistpic(request,page):
    ##查询文章
    article=Article.objects.all().order_by('id')
    pagnitor_obj=Paginator(article,6)
    page_obj=pagnitor_obj.page(page)

    page_num=page_obj.number
    start=page_num-2
    if start <= 2:
        start = 1
        end=start+5
    else:
        end = page_num+3
        if end >= pagnitor_obj.num_pages:
            end = pagnitor_obj.num_pages+1
            start = end-5
    page_range=range(start,end)

    return render_to_response("newslistpic.html",locals())

##分页
from django.core.paginator import Paginator

from .models import *

import hashlib
##密码加密   MD5
def setPassword(password):
    ###需要实例化  md5对象
    md5=hashlib.md5()
    ##对password  进行加密  参数为 bytes类型
    md5.update(password.encode())
    result=md5.hexdigest()  ##得到一个16进制的加密结果
    return result

from .forms import UserForm
def register(request):
    ##处理get请求，返回注册页面
    ##接受用户注册请求  post
    ## 将用户的数据保存到数据库

    ##判断请求方式
    # userfrom=UserForm()
    # if request.method=='POST':
    #     data=request.POST
    #     print(data)
    #     username=request.POST.get('username')
    #     password=request.POST.get('passwd')
    #     ##判断用户是否存在
    #     flag=User.objects.filter(username=username).exists()
    #     if flag:
    #         ##存在
    #         message='用户已存在'
    #         ##不存在
    #     else:
    #         ##保存数据
    #         User.objects.create(username=username,password=setPassword(password))
    #         message='注册成功'

    userfrom = UserForm()
    if request.method == 'POST':
        # data = request.POST
        # print(data)
        # username = request.POST.get('username')
        # password = request.POST.get('passwd')

        data=UserForm(request.POST)
        if data.is_valid():
            ##进行校验  成功True  失败False
            username=data.cleaned_data.get('username')
            password=data.cleaned_data.get('password')
            ##判断用户是否存在
            flag = User.objects.filter(username=username).exists()
            if flag:
                ##存在
                message = '用户已存在'
                ##不存在
            else:
                ##保存数据
                User.objects.create(username=username, password=setPassword(password))
                message = '注册成功'
        else:
            message=data.errors

    return render(request,'register.html',locals())

##json

from django.http import JsonResponse

def ajax_register(request):
    return render(request,'ajax_register.html')

##处理ajax——get请求
def ajax_get_req(request):
    """

    处理ajax的get请求
        获取到ajax的值，进行查询数据库，判断用户是否存在
    :param request:
        username  用户的账号
    :return:
        返回的是否存在结果
    """
    username=request.GET.get('username')
    print(username)
    result = {'code': 1000, 'msg':''}
    if username:
        flag=User.objects.filter(username=username).exists()
        if flag:
            # message='账号以存在'
            result={'code':1001,'msg':'账号存在'}
        else:
            # message='账号不存在'
            result={'code':1000,'msg':'账号不存在，可用'}
    else:
        # message='账号不能为空'
        result={'code':1002,'msg':'账号不能为空'}

    return JsonResponse(result)

def ajax_post_req(request):

    result={'code':1000,'msg':''}
    username=request.POST.get('username')
    password=request.POST.get('password')
    # print(username)
    # print(password)
    if username and password:
        try:
            User.objects.filter(username=username,password=setPassword(password)).exists()
            result = {'code': 1000, 'msg': '数据添加成功'}
        except:
            result={'code':1000,'msg':'数据添加失败'}
    else:
        result={'code':1001,'msg':'请求参数为空'}
    return JsonResponse(result)

from django.http import HttpResponseRedirect


def login(request):
    ##判断登录
    ##1 获取值
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username and password:
            ##校验密码是否正确
            # flag=User.objects.filter(username=username,password=setPassword(password)).exists()
            user=User.objects.filter(username=username,password=setPassword(password)).first()
            if user:
                # return HttpResponse('登录成功')
                # response=HttpResponse('登录成功')
                ##重定向  参数为要跳转的页面
                # response=HttpResponseRedirect('/app01/index')
                ##路由修改后
                response = HttpResponseRedirect('/')
                ##下发cookie session
                response.set_cookie('username',user.username)
                response.set_cookie('user_id',user.id)
                request.session['username']=user.username
                return response
            else:
                return HttpResponse("账号密码不正确")
        else:
            return HttpResponse('账号密码不能为空')

    return render(request,'login.html')

##退出登录
def logout(request):
    ##删除cookie和 session
    ##重定向到登录页
    response=HttpResponseRedirect('/login')
    response.delete_cookie('username')
    del request.session['username']

    return response

#模糊查询
def search_app01(request):
    search_key=request.Get.get('search_key')
    page=request.GET.get('page',1)
    if search_key:
        article=Article.objects.filter(title__contains=search_key).all()

        pagnitor_obj = Paginator(article, 10)
        page_obj = pagnitor_obj.page(page)
        page_num = page_obj.number
        start = page_num - 2
        if start <= 2:
            start = 1
            end = start + 5
        else:
            end = page_num + 3
            if end >= pagnitor_obj.num_pages:
                end = pagnitor_obj.num_pages + 1
                start = end - 5
        page_range = range(start, end)
    return render(request,'newslistpic.html',locals())