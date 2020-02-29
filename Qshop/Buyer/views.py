from django.shortcuts import render
import hashlib
from django.http import HttpResponseRedirect,HttpResponse
from Seller.models import *
from .models import *
# Create your views here.

def setpassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result

def loginValid(func):
    def inner(request,*args,**kwargs):
        ##校验用户身份
        cookie_email=request.COOKIES.get('buy_email')
        session_email=request.session.get('buy_email')
        if cookie_email and session_email and cookie_email==session_email:
            flag=LoginUser.objects.filter(email=cookie_email,id=request.COOKIES.get('buy_userid'),user_type=1).exists()
            if flag:
                return func(request,*args,**kwargs)
            else:
                return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/login/')
    return inner

# @loginValid
def index(request):
    """
    1、如果类型下面没有商品，类型不展示
    2、如果类型下面超过4个商品，应该展示4个
    3、如果类型下面商品 大于0 小于 4  应该展示商品

    """
    goods_type=GoodsType.objects.all()
    ## 处理返回的数据  构建数据
    ## res = [{"type":"新鲜水果.obj","goods":[goods1,goods2,goods3,goods4]},{},{}]

    res=[]
    for one in goods_type:
        goods=one.goods_set.order_by('id').all()
        if len(goods)>4:
            goods_list=goods[:4]
            res.append({'type':one,'goods_list':goods_list})
        elif len(goods)>0 and len(goods)<=4 :
            goods_list=goods
            res.append({'type':one,"goods_list":goods_list})

    return render(request,'buyer/index.html',locals())

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        if username and password:
            user=LoginUser.objects.filter(username=username,password=setpassword(password),user_type=1).first()
            if user:
                response=HttpResponseRedirect('/')
                response.set_cookie('buy_email',user.email)
                response.set_cookie('buy_username',user.username)
                response.set_cookie('buy_userid',user.id)
                request.session['buy_email']=user.email
                return response
            else:
                message='账号密码不对'
        else:
            message='参数为空'
    return render(request,'buyer/login.html',locals())

def logout(request):
    resp =  HttpResponseRedirect("/login/")
    resp.delete_cookie("buy_email")
    resp.delete_cookie("buy_username")
    resp.delete_cookie("buy_userid")
    del request.session["email"]
    return resp



def register(request):
    if request.method=='POST':
        username=request.POST.get('user_name')
        password=request.POST.get('pwd')
        repassword=request.POST.get('cpwd')
        email=request.POST.get('email')
        if email and password and password==repassword:
            LoginUser.objects.create(email=email,password=setpassword(password),username=username)
            return HttpResponseRedirect("/login/")
        else:
            message='参数为空'
    return render(request,'buyer/register.html',locals())



def cart(request):

    return render(request,'buyer/cart.html')


def detail(request):
    goods_id=request.GET.get('goods_id')
    goods=Goods.objects.filter(id=goods_id).first()
    return render(request, 'buyer/detail.html',locals())


def list(request):

    kywards=request.GET.get('kywards')
    req_type=request.GET.get('req_type')
    # ##判断请求方式
    if req_type=='findall':
    #     ##查看跟多
    #         ##req__type 应为商品的id
        goods =Goods.objects.filter(goods_type_id=kywards)
    else:
        ##搜索
    #         ##kywards为 商品名字  模糊查询
        goods=Goods.objects.filter(goods_name__contains=kywards).order_by('-goods_pro_time')
        goods_new=goods[:2]

    return render(request, 'buyer/list.html',locals())

def get_order_no():
    import uuid
    order_no=str(uuid.uuid4()).replace('-','')
    return order_no


@loginValid
def place_order(request):
    ##保存数据
    ## 获取 买家的user_id
    user_id = request.COOKIES.get("buy_userid")
    goods_id = request.GET.get("goods_id")
    goods_count = int(request.GET.get("goods_count"))
    ## 查找商品
    goods = Goods.objects.get(id=goods_id)
    ##payorder
    payorder=PayOrder()
    payorder.order_number = get_order_no()
    payorder.order_status = 1  ### 未支付状态
    payorder.order_total = goods_count * goods.goods_price
    payorder.order_user_id = int(user_id)
    payorder.save()

    order_info = OrderInfo()
    order_info.order = payorder
    order_info.goods = goods
    order_info.goods_price = goods.goods_price

    ## 店铺的信息 通过商品寻找 店铺
    order_info.store = goods.goods_store
    order_info.goods_count = goods_count
    order_info.goods_total_price = goods_count * goods.goods_price
    order_info.save()


    return render(request, 'buyer/place_order.html',locals())

def user_center_info(request):
    return render(request, 'buyer/user_center_info.html')


def user_center_order(request):
    return render(request, 'buyer/user_center_order.html')

def user_center_site(request):
    return render(request, 'buyer/user_center_site.html')


##聚合查询
from django.db.models import Sum,Count
def goods_test(request):
    order_id=21
    pay_order=PayOrder.objects.get(id=order_id)
    ##聚合方法  aggregate  返回值是字典
    ##key 默认的   可以修改
    sum_goods=pay_order.orderinfo_set.aggregate(Sum('goods_count'),
                                                mycount=Count('id'))


    return render(request,'buyer/goods_test.html',locals())


from Qshop.settings import alipay
def alipay_order(request):
    ##获取订单  payorder_id
    payorder_id=request.GET.get('payorder_id')
    payorder=PayOrder.objects.get(id=payorder_id)
    ##3  实例化订单
    order_string = alipay.api_alipay_trade_page_pay(
        subject='生鲜交易',  ##主题
        out_trade_no=payorder.order_number,  ##订单号
        total_amount=str(payorder.order_total),  ##交易金额  字符串
        return_url='http://127.0.0.1:8000/buyer/pay_result/',  ##回调地址
        notify_url=None  ##通知
    )

    ##4 返回支付宝支付的url

    result = 'https://openapi.alipaydev.com/gateway.do?' + order_string
    return HttpResponseRedirect(result)



##接收支付宝的处理结果
def pay_result(request):
    out_trade_no=request.GET.get("out_trade_no")

    payorder=PayOrder.objects.get(order_number=out_trade_no)
    payorder.order_status=2
    payorder.save()

    return render(request,'buyer/pay_result.html',locals())



