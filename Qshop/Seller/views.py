from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
# Create your views here.
import hashlib

##密码加密
def setpassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result


def register(request):
    # print(request.POST)
    if request.method=='POST':
        password=request.POST.get('password')
        repassword=request.POST.get('repassword')
        email=request.POST.get('email')
        if email and password and password==repassword:
            LoginUser.objects.create(email=email,password=setpassword(password),user_type=0)
            return HttpResponseRedirect("/seller/login/")
        else:
            message='参数为空'

    return render(request, 'seller/register.html', locals())


def login(request):
    # print(request.POST)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user=LoginUser.objects.filter(email=email,password=setpassword(password),user_type=0).first()
            if user:
                response=HttpResponseRedirect('/seller/index')
                response.set_cookie('email',user.email)
                response.set_cookie('userid',user.id)
                request.session['email']=user.email
                return response
            else:
                message='账号密码不对'
        else:
            message='参数为空'

    return render(request, 'seller/login.html', locals())


def loginValid(func):
    def inner(request,*args,**kwargs):
        ##校验用户身份
        cookie_email=request.COOKIES.get('email')
        session_email=request.session.get('email')
        if cookie_email and session_email and cookie_email==session_email:
            flag = LoginUser.objects.filter(email=cookie_email, id=request.COOKIES.get('userid'), user_type=0).exists()
            if flag:
                return func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect('/seller/login/')
        else:
            return HttpResponseRedirect('/seller/login/')
    return inner

# @loginValid
def index(request):

    return render(request,'seller/index.html')

def logout(request):
    ##删除cookie和 session
    ##重定向到登录页
    response=HttpResponseRedirect('/seller/login')
    response.delete_cookie('email')
    del request.session['email']

    return response


def base(request):

    return render(request, 'seller/base.html')

##商品列表页面显示
from django.core.paginator import Paginator
@loginValid
def goods_list(request,status,page=1):
    ##根据状态查询商品
    ##status  状态表示  0下架   1在售
    # goods=Goods.objects.filter(goods_status=status).order_by('id')
    goods=Goods.objects.filter(goods_status=status,goods_store_id=request.COOKIES.get('userid')).order_by('id')
    goods_obj=Paginator(goods,8)
    goods_list=goods_obj.page(page)

    # return render(request,'goods_list.html',locals())
    return render(request, 'seller/goods_list.html',locals())

##修改商品状态
def goods_status(request,id,status):
    ##获取商品id
    ##上架  下架
    """

    :param request:
    :param id: 商品id
    :return status:
            up 上架
            down 下架
    """
    goods=Goods.objects.get(id = id)
    if status=='up':
        goods.goods_status=1
        goods.save()
    else:
        goods.goods_status=0
        goods.save()

    url=request.META.get('HTTP_REFERER')   ##得到请求地址
    print(url)
    # return HttpResponseRedirect('/loginuser/goods_list/1/1/')
    return HttpResponseRedirect(url)

@loginValid
##个人中心
def user_profile(request):
    ##返回用户的信息
    ##从session  和cookie 这里获取登陆的用户
    userid=request.COOKIES.get('userid')
    user=LoginUser.objects.get(id=userid)
    ##处理post请求
    if request.method=="POST":
        data=request.POST
        user.email=data.get('email')
        user.phone_number=data.get('phone_number')
        user.username=data.get('username')
        user.age=data.get('age')
        user.gender=data.get('gender')
        user.address=data.get('address')

        if request.FILES.get('img'):
            user.phono=request.FILES.get("img")
        user.save()

    return render(request,'seller/user_profile.html',locals())

@loginValid
##录入商品
def goods_add(request):
    goods_type=GoodsType.objects.all()
    if request.method=='POST':
        user_id=request.COOKIES.get('userid')
        data=request.POST
        goods=Goods()
        goods.goods_number = data.get("goods_number")
        goods.goods_name = data.get("goods_name")
        goods.goods_price = data.get("goods_price")
        goods.goods_count = data.get("goods_count")
        goods.goods_location = data.get("goods_location")
        goods.goods_safe_date = data.get("goods_safe_date")
        # goods.goods_picture = data.get("goods_number")
        goods.goods_type_id = int(data.get("goods_type"))
        goods.goods_store = LoginUser.objects.get(id=user_id)
        goods.goods_picture = request.FILES.get("img")
        goods.save()
    return render(request,'seller/goods_add.html',locals())



##添加商品类型
# def add_label(request):
#
#     GoodsType.objects.create(type_label='新鲜水果',type_description='新鲜水果',type_picture='img/banner01.jpg')
#     GoodsType.objects.create(type_label='海鲜水产',type_description='海鲜水产',type_picture='img/banner02.jpg')
#     GoodsType.objects.create(type_label='猪牛羊肉',type_description='猪牛羊肉',type_picture='img/banner03.jpg')
#     GoodsType.objects.create(type_label='禽类蛋品',type_description='禽类蛋品',type_picture='img/banner04.jpg')
#     GoodsType.objects.create(type_label='新鲜蔬菜',type_description='新鲜蔬菜',type_picture='img/banner05.jpg')
#     GoodsType.objects.create(type_label='速冻食品',type_description='速冻食品',type_picture='img/banner06.jpg')
#
#     return HttpResponse('类型')