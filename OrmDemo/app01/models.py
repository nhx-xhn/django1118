from django.db import models

# Create your models here.
class User(models.Model):
    ##写属性
    ##主键  id   django  的orm会自动创建主键
    # id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=32,verbose_name='用户的名')
    age=models.IntegerField(verbose_name='用户的年龄')
    phone=models.CharField(max_length=11,verbose_name='用户的手机号')
    email=models.EmailField(default="111@qq.com",verbose_name='用户的邮箱')

    class Meta:
        db_table='user'   ##改表名
        # ordering=['age']
        verbose_name='用户'  ##改中文
        verbose_name_plural='用户'  ##去掉复数



##创建超级用户
class Subject(models.Model):
    name=models.CharField(max_length=32,verbose_name='学科的名字')
    start_time=models.DateField(verbose_name='开始时间')
    class Meta:
        db_table='subject'
        verbose_name='学科'
        verbose_name_plural='学科'




class Publish(models.Model):
    name=models.CharField(max_length=32,verbose_name='出版社名字')
    address=models.CharField(max_length=32,verbose_name='出版社地址')

    class Meta:
        db_table='publish'
        verbose_name_plural='出版社'



class Book(models.Model):
    name=models.CharField(max_length=32,verbose_name='书名')
    num=models.IntegerField(verbose_name='数量')
    price=models.IntegerField(verbose_name='价格')
    publish=models.ForeignKey(to=Publish,to_field='id',on_delete=models.CASCADE)

    class Meta:
        db_table='book'
        verbose_name_plural='书'


##Foreignkey 字段属性
"""
to 代表 和哪个表产生关联
to_fiedl  代表和关联表的哪个字段关联  可以不填  默认是id
on_delete  代表关联表中的数据被删的时候  被关联的表做什么操作  
        models.CASCADE默认删除，当关联表中数据被删后，关联数据删除
        models.PROTECT  保护
"""



class Preson(models.Model):
    name=models.CharField(max_length=32,verbose_name='学生姓名')
    age=models.IntegerField(verbose_name='学生年龄')
    class Meta:
        db_table='preson'


class Teacher(models.Model):
    name=models.CharField(max_length=32,verbose_name='老师姓名')
    gender=models.IntegerField(verbose_name='性别')   ##1 男  0女
    age=models.IntegerField(verbose_name='年龄')
    preson=models.ManyToManyField(to=Preson)
    class Meta:
        db_table='teacher'


"""
ManyToManyField: 创建多对多关系的属性
to = 类名  和那种表是多对多的关系
多对多的关系属性 ManyToManyField 可以放在两种表的任意一张表，没有影响，影响的是 关系表之间的正向和反向的关系
多对多关系的操作和一对多类似，关键搞明白 正向和反向
"""



