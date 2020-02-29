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


def add_app01(request):
    for i in range(100):
        article=Article()
        article.title='title_%s'% i
        article.content='content_%s'% i
        article.description='description_%s'% i
        article.author=Author.objects.get(id=1)
        article.save()
        article.type.add(Type.objects.get(id=1))
        article.save()
    return HttpResponse("add_app01")

##分页
from django.core.paginator import Paginator

def fy_test(request):
    article=Article.objects.all().order_by('id')
    # print(article)
    ##paginator  是数据集  每页显示的条数
    paginator_obj=Paginator(article,10)
    print(paginator_obj)
    # print(paginator_obj.count)  ## 数据总条数
    # print(paginator_obj.num_pages)  ## 总页数
    # print(paginator_obj.page_range)  ## renge(1,12)

    page_obj=paginator_obj.page(10)
    print(page_obj)    #<page  1 of 11>
    ## 遍历循环  得到分页后的数据
    # for one in page_obj:
    #     print(one)

    # print(page_obj.has_next())  ##是否有下一页
    # print(page_obj.has_previous())  ##是否有上一页
    # print(page_obj.number)   ##返回当前所在页码
    # print(page_obj.previous_page_number())  ##上一页的页码
    # print(page_obj.next_page_number()) ## 下一页的页码
    # print(page_obj.has_other_pages())  ##是否有其他页码
    #
    return HttpResponse("fy_test")






from .models import *

def choices_text(request):
    date=Author.objects.get(id=1)
    print(date.gender)
    gender=date.get_gender_display()  ###get_字段_display  将属性拿出来
    print(gender)

    return HttpResponse('choices_text')



def request_demo(request):
    ##学习请求 提供的方法
    # print(dir(request))

    # print(request.COOKIES)  ##标识用户身份的
    # print(request.FILES)   ##上传的文件  如 图片 文档
    ##GET  get请求传递的参数
    # name=request.GET.get('name')
    # age=request.GET.get('age')
    # print(name)
    # print(age)

    # print(request.method)  ##获取请求的的 方式 GET POST
    # print(request.scheme)   ##请求的协议
    # print(request.path)  ##请求的路径  路由
    # print(request.META)  ##请求的信息
    # print(request.META.get('OS')  ##请求的系统
    # print(request.META.HTTP_REFERER)  ## 请求的来源
    # print(request.META.HTTP_HOST)  ##请求的主机 + post


    return HttpResponse('request_demo')



# def get_test(request):
    # data=request.GET
    # print(data)
    # name=request.GET.get('name')
    # age=request.GET.get('age')

    # return HttpResponse("get_test,姓名为{},年龄为{}".format(name,age))

# def post_demo(request):
    # data=request.POST
    # print(data)
    # name=request.POST.get('name')
    # age=request.POST.get('age')

    # return HttpResponse('post_demo,姓名{},年龄{}'.format(name,age))





def getdemo(request):

    ##视图完成的功能
      ## 提供form表单页面
      ##  获取用户比偶啊但中输入的数据  进行处理  并返回结果



    # data=request.GET
    # print(data)
    # search=request.GET.get('search')
    # print(search)
    # data=request.GET.getlist('search')
    # print(data)

    ##接收数据  处理请求  返回响应
    ## 获取到关键词
    search = request.GET.get('search')
    ##查询数据库  得到文章标题
    if search:
        ##查询数据库
        article=Article.objects.filter(title__contains=search).values('title')
        if len(article)==0:
            article='无对应文章'

    ##返回结果

    return render_to_response('getdemo.html',locals())



def qqtest(request):

    return render_to_response('qqtest.html')

import hashlib
##密码加密   MD5
def setPassword(password):
    ###需要实例化  md5对象
    md5=hashlib.md5()
    ##对password  进行加密  参数为 bytes类型
    md5.update(password.encode())
    result=md5.hexdigest()  ##得到一个16进制的加密结果
    return result


##csrf验证
def postdemo(request):
    username=request.POST.get('username')
    password=request.POST.get('passwd')
    print(username)
    print(password)

    # return render_to_response('postdemo.html')
    return render(request,'postdemo.html')

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


def zhuce(request):
    if request.method=='POST':
        data=request.POST
        print(data)
        username=request.POST.get('form-username')
        password=request.POST.get('form-password')
    #     ##判断用户是否存在
    #
        flag=User.objects.filter(username=username).exists()
        if flag:
    #         ##存在
            message='用户已存在'
    #         ##不存在
        else:
    #
    #         ##保存数据
            User.objects.create(username=username,password=password)
            message='注册成功'
    return render(request,'zhuce.html',locals())



def ajaxdemo(request):
    return render(request,'ajaxdemo.html')


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


##下发cookie
def set_cookie(request):
    #####set_cookie方法：
        ##max_age 是cookie的寿命 秒
        ##expires  cookie到期时间  和max_age二选其一
        ##path  路径  设置cookie生效的范围
        ##domain=None  生效的域名
        ##secure=False  是否使用加密方式保存cookie
        ##samesite=None    相同的网站使用cookie
    # return HttpResponse()
    # response=HttpResponse("设置cookie")
    response=render(request,'index.html')
    ##设置cookie
    ##如果要多个cookie  就在写一行   cookie中不要写中文
    response.set_cookie('username','zhangsan',max_age=10)
    response.set_cookie('age',23)
    return response

def get_cookie(request):
    ##获取cookie
    data=request.COOKIES
    username=request.COOKIES.get("username")
    age=request.COOKIES.get("age")
    print(username)
    print(age)
    return HttpResponse("获取cookie")


def delete_cookie(request):

    response=HttpResponse("删除cookie")
    response.delete_cookie('username')
    response.delete_cookie('age')
    return response
    # return HttpResponse()



def set_session(request):

    ##设置session
    request.session['username']='zhangsan'


    return HttpResponse('设置session')


def get_session(request):

    username=request.session.get('username')
    return HttpResponse(username)


def delete_session(request):
    username=request.session.get('username')
    print(username)

    del request.session['username']

    return HttpResponse('删除ssession')

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