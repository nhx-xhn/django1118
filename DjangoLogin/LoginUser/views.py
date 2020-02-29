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
    print(request.POST)
    password=request.POST.get('password')
    repassword=request.POST.get('repassword')
    email=request.POST.get('email')
    if email and password and password==repassword:
        LoginUser.objects.create(email=email,password=setpassword(password))
        return HttpResponseRedirect("/login/")
    else:
        message='参数为空'

    return render(request,'register.html',locals())


def login(request):
    # print(request.POST)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user=LoginUser.objects.filter(email=email,password=setpassword(password)).first()
            if user:
                response=HttpResponseRedirect('/')
                response.set_cookie('email',user.email)
                request.session['email']=user.email
                return response
            else:
                message='账号密码不对'
        else:
            message='参数为空'




    return render(request,'login.html',locals())


def loginValid(func):
    def inner(request,*args,**kwargs):
        ##校验用户身份
        cookie_email=request.COOKIES.get('email')
        session_email=request.session.get('email')
        if cookie_email and session_email and cookie_email==session_email:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/login/')
    return inner

@loginValid
def index(request):

    return render(request,'index.html')

def logout(request):
    ##删除cookie和 session
    ##重定向到登录页
    response=HttpResponseRedirect('/login')
    response.delete_cookie('email')
    del request.session['email']

    return response


def base(request):

    return render(request,'base.html')

##商品列表页面显示
from django.core.paginator import Paginator
@loginValid
def goods_list(request,status,page=1):
    ##根据状态查询商品
    ##status  状态表示  0下架   1在售
    goods=Goods.objects.filter(goods_status=status).order_by('id')
    goods_obj=Paginator(goods,8)
    goods_list=goods_obj.page(page)

    # return render(request,'goods_list.html',locals())
    return render(request,'goods_list.html')

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


# import random
# ## 添加 100 商品
def add_goods(request):
#     # 循环
#     goods_name = "萝卜、马铃薯、藕、甘薯、山药、芋头、茭白、苤蓝、慈姑、洋葱、生姜、大蒜、蒜薹、韭菜花、大葱、韭黄、冬瓜、南瓜、西葫芦、丝瓜、黄瓜、茄子、西红柿、苦瓜、辣椒、玉米、小瓜、菠菜、油菜、卷心菜、苋菜、韭菜、蒿菜、香菜、芥菜、芥兰"
#     goods_name = goods_name.split("、")
#     goods_address = "石家庄、沈阳、哈尔滨、杭州、福州、济南、广州、武汉、成都、昆明、兰州、台北、南宁、银川、太原、长春、南京、合肥、南昌、郑州、长沙、海口、贵阳、西安、西宁、呼和浩特、拉萨、乌鲁木齐"
#     goods_address = goods_address.split("、")
#     for i,j in enumerate(range(100),1):
#         goods = Goods()
#         # goods_number 为  00001    00002   00100
#         goods.goods_number = str(i).zfill(5)
#         goods.goods_name = random.choice(goods_address)+random.choice(goods_name)
#         goods.goods_price = round(random.random()*100,2)  ## 保留小数点 2位
#         goods.goods_count = random.randint(1,100)    ##
#         goods.goods_location = random.choice(goods_address)
#         goods.goods_safe_date = random.randint(1,32)
#         goods.save()
    return HttpResponse("add goods")







def goods_list_api(request,status,page=1):
    ##根据状态查询商品
    ##status  状态表示  0下架   1在售
    goods = Goods.objects.filter(goods_status=status).order_by('id')
    goods_obj = Paginator(goods, 8)
    goods_list = goods_obj.page(page)

    result={'code':10000,'mas':'成功','data':''}
    res=[]
    for one in goods_list:
        res_dict={
            'id':one.id,
            'goods_number':one.goods_number,
            'goods_name':one.goods_name,
            'goods_price':one.goods_price,
            'goods_count':one.goods_count,
            'goods_location':one.goods_location,
            'goods_safe_date':one.goods_safe_date,
            'goods_pro_time':one.goods_pro_time,
            'goods_status':one.goods_status,
        }
        res.append(res_dict)
        result['data']=res
        result['page']=page
        result['page_range']=list(goods_obj.page_range)

    # return JsonResponse(result)
    ##解决跨域请求
    response=JsonResponse(result)
    response['Access-Control-Allow-Origin']= '*'
    return response



def goods_list_ajax(request):
    return render(request,'ajax_goods_list.html')


def vue_demo(request):
    return render(request,'vue_demo.html')

from django.views import View
class GoodsView(View):

    def __init__(self):
        super(GoodsView, self).__init__()
        self.result={
            'version':'v1',
            'methods':'',
            'data':'',
            'code':'',
        }
        self.obj=Goods


    ##get
    def get(self,request):
        result={'methods':'get请求'}

        ##获取id
        id = request.GET.get('id')
        if id:
            goods=self.obj.objects.filter(id=id).first()
            data={
                "goods_number": goods.goods_number,
                "goods_name": goods.goods_name,
                "goods_price": goods.goods_price,
                "goods_count": goods.goods_count,
                "goods_location": goods.goods_location,
                "goods_safe_date": goods.goods_safe_date,
                "goods_status": goods.goods_status,
            }
            # result['data']=data

        else:
            goods=self.obj.objects.all()
            data=[]
            for one in goods:
                res={
                    "goods_number": one.goods_number,
                    "goods_name": one.goods_name,
                    "goods_price": one.goods_price,
                    "goods_count": one.goods_count,
                    "goods_location": one.goods_location,
                    "goods_safe_date": one.goods_safe_date,
                    "goods_status": one.goods_status,
                }
                data.append(res)
                # result["data"]=data
                ##有了__init__之后
        self.result['methods']='get请求'
        self.result['data']=data
        self.result['code']=10000
        self.result['msg']='请求成功'

        # return JsonResponse(result)
        return JsonResponse(self.result)

    ##post
    def post(self,request):
        result={'methods':'post请求'}
        data=request.POST
        goods=Goods()
        goods.goods_number=data.get('goods_number')
        goods.goods_name=data.get('goods_name')
        goods.goods_price=data.get('goods_price')
        goods.goods_count=data.get('goods_count')
        goods.goods_location=data.get('goods_location')
        goods.goods_safe_date=data.get('goods_safe_date')
        goods.save()

        self.result["methods"] = "post请求"
        self.result["data"] = {"id": goods.id}
        self.result["code"] = 10000
        self.result["msg"] = "保存数据成功"

        return JsonResponse(self.result)

    ##put   put请求在body里
    def put(self,request):
        import json

        # data=request.body
        # data=data.decode
        # data=json.loads(data)
        # id=data.get('id')
        # print(id)
        data=json.loads(request.body.decode())
        id=data.get('id')
        goods_name=data.get('goods_name')
        flag=Goods.objects.filter(id=id).exists()
        if flag:
            Goods.objects.filter(id=id).update(goods_name=goods_name)
            
            self.result['methods']='put请求'
            self.result['data']={'id':id}
            self.result['code']=10000
            self.result['msg']='修改成功'
        else:
            self.result['methods'] = 'put请求'
            self.result['data'] = {'id': id}
            self.result['code'] = 10001
            self.result['msg'] = '商品不存在'

        # result={'methods':'put请求'}
        return JsonResponse(self.result)

    ##delete
    def delete(self,request):
        import json
        data=json.loads(request.body.decode())
        id =data.get('id')
        Goods.objects.filter(id=id).delete()
        self.result['methods'] = 'delete请求'
        self.result['data'] = {'id': id}
        self.result['code'] = 10000
        self.result['msg'] = '删除成功'

        # result={'methods':'delete请求'}
        return JsonResponse(self.result)

# from django.middleware.csrf import get_token
# ## 获取csrftokoen
# def gettoken(request):
#     token = get_token(request)
#     return JsonResponse({"token":token})



from .serializers import GoodsSerializers
from rest_framework import mixins,viewsets


class GoodsViews(mixins.CreateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    queryset=Goods.objects.all()
    serializer_class=GoodsSerializers





