from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def adduser(request):
    ##orm操作数据库

    ##增加 save
    #第一种

    # user=User()
    # user.user_name='lisi'
    # user.age=18
    # user.phone='1520123012'
    # user.email='lisi@012.com'
    # user.save()

    #第二种
    # user=User(user_name='laoba',age=20,phone='152012023',email='wangwu@0223.com')
    # user.save()

    ##  create
    #能增加数据
    #会将增加的数据返回
    #第一种
    # User.objects.create(user_name='zhaoliu',age=21,phone='152012312',email='zhaoliu@152.com')

    #第二种  字典
    # params=dict(user_name='laoqi',age=22,phone='152012312',email='laoqi@152.com')
    # User.objects.create(**params)  ##   **是解包

    return HttpResponse("add_user")


##查询
def getuser(request):
    ##1.  all
    ##会返回符合条件的所有数据  返回的是QuerySet
    ##可以用循环遍历查看每一个数据

    # user=User.objects.all()
    # print(user)
    # for one in user:
    #     print(one)  ##
    #     print(one.user_name)
    #
    # print(user[0].age)


    ##  注意  每次用别的models时先把它导入进来
    # sub=Subject.objects.all()
    # print(sub)


    ##get方法
    ##返回符合条件的数据
    ##返回的值是  对象
    #方法一
    #user=User.objects.get(id=3)
    # print(user)
    ##方法二
    # user = User.objects.get(user_name='wangwu')
    # print(user)
    # print(user.user_name)
    # user=User.objects.get(age=22)
    # print(user)


    ##filter 方法   过滤筛选
    ##返回符合条件的说有数据
    ##返回的是queryset
    # user=User.objects.filter(age=21)
    # print(user)
    # for one in user:
    #     print(one)
    #     print(one.user_name)
    # print(user[0].age)

    ##exclude  返回不符合条件的数据
    ##返回的书qureyset
    # user=User.objects.exclude(age=21)
    # print(user)
    # for one in user:
    #     print(one)
    #     print(one.user_name)


    ##first  返回符合条件的第一个数据
    ##last  返回符合条件的最后一条数据
    ##返回的是对象
    # user=User.objects.filter(age=21).first()
    # print(user)
    # user = User.objects.filter(age=21).last()
    # print(user)



    ##order_by  排序
    ###第一种
    ##升序
    # user=User.objects.filter(age=21).order_by("id").first()
    # print(user)

    ##降序
    # user=User.objects.filter(age=21).order_by("-id").first()
    # print(user)

    ##第二种
    ##在models的元数据 里加上条件


    ##  revers反转
    ##使用条件   使用前结果必须是排序的，可以使用order_by  或ordering  (ordering是在元数据里添加)
    # user=User.objects.order_by('id').reverse()
    # print(user)
    # user=User.objects.order_by('id').all()
    # print(user)


    ##values
    ##返回的是queryset  比较特殊  得到的是[{}{}]
   ##三种
    # user=User.objects.values()
    # print(user)
    # for one in user:
    #     print(one)
    #     print(one['age'])
    # print(user[0]['user_name'])

    # user=User.objects.values('phone')
    # print(user)

    # user=User.objects.filter(age=21).all().values('user_name','age')
    # print(user)


    ##count  计数
    ##返回的是  int类型  不能遍历
    # user=User.objects.filter(age=21).count()
    # print(user)
    # user=User.objects.count()
    # print(user)


    ##exists  查看数据是否存在
    ##返回的是布尔
    # user=User.objects.filter(user_name="wangwu").exists()
    # print(user)


    ##切片
    # user=User.objects.all()[0:2]
    # print(user)
    # for one in user:
    #     print(one)
    #     print(one.age)
    # print(user[0].user_name)


    return HttpResponse("get_user")

def update_user(request):
    ###跟新数据

    ## 1.   save  ##先查到数据
    # user=User.objects.get(id=2)
    # user.user_name='python'
    # user.save()
    #
    # user=User.objects.filter(age=19).first()
    # user.user_name='java'
    # user.save()

    # user = User.objects.filter(age=20).first()   #返回的是Qeryset
    # for one in user:
    #     one.user_name='php'
    #     one.save()


    ##update
    # User.objects.filter(id=2).update(name='小二')

    Book.objects.filter(id=1).update(num=132,price=241)
    Book.objects.filter(id=2).update(num=162,price=353)
    Book.objects.filter(id=3).update(num=24,price=12)
    Book.objects.filter(id=4).update(num=67, price=143)
    Book.objects.filter(id=5).update(num=24, price=98)

    return HttpResponse('update_user')


def delete_user(request):
    ##delete  删除
    ##queryset
    # User.objects.filter(id=4).delete()
    ##对象
    # User.objects.get(id=11).delete()

    return HttpResponse('delete_user')


def mohu_user(request):
    ##查询范围
    ##__lt  小于
    # date=User.objects.filter(id__lt=10).all()
    # print(date)
    ##__gt  大于
    # date=User.objects.filter(id__gt=10).all()
    # print(date)
    ##__lte  小于等于
    # date = User.objects.filter(id__lte=10).all()
    # print(date)
    ##__gte  大于等于
    # date=User.objects.filter(id__gte=10).all()
    # print(date)
    ##__in  在这个范围里，
    # date = User.objects.filter(id__in=[4,10,14]).all()
    # print(date)
    ##__contains  模糊查新
    # date = User.objects.filter(user_name__contains='ao').all()
    # print(date)
    ##__icontains  忽略大小写
    # date=User.objects.filter(user_name__icontains="lao").all()
    # print(date)
    ##__startwith  开头
    # date=User.objects.filter(user_name__startwith='lao').all()
    # print(date)
    ##__endwith  结尾
    # date = User.objects.filter(user_name__endwith='lao').all()
    # print(date)

    return HttpResponse('mohu_user')


def add_f(request):
    ##Publish添加数据

    # Publish.objects.create(name='北京出版社',address='北京')
    # Publish.objects.create(name='上海出版社', address='上海')
    # Publish.objects.create(name='深圳出版社', address='深圳')


    ##book添加数据

    #第一种
    # Book.objects.create(name='python爬虫',publish_id='3')
    # 正向   从外键表到关联表
    #第二种######
    # publish_obj=Publish.objects.filter(name='深圳出版社').first()
    # Book.objects.create(name='python爬虫',pub=publish_obj)


    ##反向从关联表到外键表   set
    ##先拿到punlish的对象
    # publish_obj=Publish.objects.filter(name='北京出版社').first()
    # publish_obj.book_set.create(name='python web')


    return HttpResponse('一对多关系的增加操作')


def get_f(request):
    ##一对多查询
    ##查询北京出版社的书
    # #########
    # publish_obj=Publish.objects.filter('name=北京出版社').first()
    # book_obj=Book.objects.filter(publish_id=publish_obj.id).all()
    # print(book_obj.name)


    ##查询python 全栈  是哪个出版社
    # book_obj=Book.objects.filter(name='python全栈').first()
    # pub_obj=Publish.objects.filter(id=book_obj.publish_id)
    # print(pub_obj.name)


    ##正向
    #查询python全栈 是哪个出版社
    # book_obj=Book.objects.filter(name='python全栈').first()
    # pub_obj=book_obj.publish
    # print(pub_obj)
    # print(pub_obj.name)

    ##反向
    # pub_obj=Publish.objects.filter(name='北京出版社').first()
    # book_obj=pub_obj.book_set.values('name')
    # print(book_obj)

    return HttpResponse('一对多关系查询')



def update_f(request):
    # pub_obj=Publish.objects.filter(name='上海出版社').first()
    # Book.objects.filter(name='python爬虫').update(publish_id=pub_obj.id)

    ##正向
    # pub_obj = Publish.objects.filter(name='上海出版社').first()
    # Book.objects.filter(name='python爬虫').update(publish_id=pub_obj.id)


    ##反向
    #  publish_obj = Publish.objects.filter(name="北京出版社").first()  
    #  book_obj = Book.objects.filter(name="python").first()  
    #  publish_obj.book_set.set([book_obj])   #列表里可以写多个


    return HttpResponse('一对多修改')



def delete_f(request):
    ## 删除  
    ## 由于设置了 on_delete=models.CASCADE 在删除关联表数据时，从表中关联数据也会被删除掉  
    #  Publish.objects.filter(name="上海出版社").delete()  
    # Book.objects.filter(name="python全栈").delete()

    return HttpResponse('一对多删除')



##多对多增加

def add_many(request):
    ##  add  create
    ##增加学生
    # Preson.objects.create(name='小五',age=13)
    ##增加老师
    # Teacher.objects.create(name='老李',gender=1,age=45)
    # Teacher.objects.create(name='老宋', gender=1, age=45)
    # Teacher.objects.create(name='老边', gender=1, age=45)

    ##add 正向  针对已经存在的数据 创建关系
    # teacher=Teacher.objects.filter(name='老李').first()
    # preson=Preson.objects.filter(name='小李').first()
    # teacher.preson.add(preson)

    # 2·
    # teacher = Teacher.objects.filter(name='老李').first()
    # preson1=Preson.objects.filter(name='小三').first()
    # preson2 = Preson.objects.filter(name='小五').first()
    # teacher.preson.add(preson1,preson2)

    ##反向
    # preson_obj=Preson.objects.filter(name='小二').first()
    # teacher_obj1=Teacher.objects.filter(name='老王').first()
    # teacher_obj2 = Teacher.objects.filter(name='老边').first()
    # preson_obj.teacher_set.add(teacher_obj1,teacher_obj2)
    
    
    ##create  正向  新增数据  并且创建关系
    ##1·
    # teacher=Teacher.objects.filter(name='老宋').first()
    # teacher=Preson.create(name='小四',age=23)

    ##反向


    return HttpResponse('多对多增加')


def get_many(request):
    ##查询
    ##正向
    # teacher_obj=Teacher.objects.filter(name='老边').first()
    # preson_obj=teacher_obj.preson.all().values('name')
    # print(preson_obj)

    ##反向
    # preson_obj=Preson.objects.filter(name='小二').first()
    # teacher_obj=preson_obj.teacher_set.all()
    # print(teacher_obj)

    return HttpResponse('多对多查询')


def update_many(request):
    ##修改  set
    ##正向
    # teacher_obj=Teacher.objects.filter(name='老边').first()
    # preson_obj1=Preson.objects.filter(name='小二').first()
    # preson_obj2 = Preson.objects.filter(name='小四').first()
    # preson_obj3 = Preson.objects.filter(name='小五').first()
    # teacher_obj.preson.set([preson_obj1,preson_obj2,preson_obj3])

    ##反向
    # preson_obj=Preson.objects.filter(name='小李').first()
    # teacher_obj=Teacher.objects.filter(name='老王').first()
    # teacher_obj1= Teacher.objects.filter(name='老宋').first()
    # preson_obj.teacher_set.set([teacher_obj,teacher_obj1])
    ##最后一步还可以放id
    ##preson_obj.teacher_set([1,2,3])

    return HttpResponse('多对多修改')


def delete_many(request):
    ##remove解除指定的数据间的关系
    ##正向
    # teacher_obj=Teacher.objects.get(id=2)
    # preson_obj=Preson.objects.get(id=3)
    # teacher_obj.preson.remove(preson_obj)

    ##反向
    # teacher_obj=Teacher.objects.get(id=4)
    # preson_obj=Preson.objects.get(id=7)
    # preson_obj.teacher_set.remove(teacher_obj)

    ##clear  消除某个数据的所有关系
    ##正向
    # teacher_obj=Teacher.objects.get(id=2)
    # teacher_obj.preson.clear()

    ##反向
    # preson_obj=Preson.objects.get(id=2)
    # preson_obj.teacher_set.clear()

    ##delete
    # Preson.objects.filter(id=1).delete()

    return HttpResponse('多对多删除')


###聚合查询
from django.db.models import Sum,Max,Min,Avg,Count
##依赖 aggregate   是django ORM里的终止语句

def juhe(request):
    ##返回字典   里面的key是自动生成的  计算的字段__使用的聚合方法
    ## values 是计算的结果
    # date=Preson.objects.all().aggregate(Max('age'))
    # print(date)
    # print(date['age__max'])
    ##  key 名字可以自己设置
    # date=Preson.objects.all().aggregate(min__age=Min('age'),sum__age=Sum('age'))
    # print(date)
    # print(date['min__age'],date['sum__age'])

    return HttpResponse("聚合查询")


###F  和  Q 对象
from django.db.models import F,Q

def tiaojian(request):
    ## F  能够比较同一张表中两个字段的大小
    ##  查询  num 大于 price  的书名
    # date = Book.objects.filter(num__gt=F('price')).values('name')
    # print(date)

    # date = Book.objects.filter(price__gt=F('num')*2).values('name')
    # print(date)


    ## Q能实现  and  or  not 关系
    ##查询条件为 num>10 and price>10
    # date=Book.objects.filter(num__gt=10,price__gt=10).all()
    # print(date)
    ##and  &
    # date=Book.objects.filter(Q(num__gt=10)&Q(price__gt=10)).all()
    # print(date)
    ##or |
    # date = Book.objects.filter(Q(num__gt=10) | Q(price__gt=10)).all()
    # print(date)
    ##not  ~
    # date = Book.objects.filter(Q(num__gt=10) ~ Q(price__gt=10)).all()
    # print(date)



    return HttpResponse('条件查询')






