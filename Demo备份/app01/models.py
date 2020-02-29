from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

# class app01(models.Model):



GENDER_STATUS=(
    (0,'女'),
    (1,'男')
)

class Author(models.Model):
    # id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name='作者名字')
    # gender=models.CharField(max_length=32,verbose_name='性别')
    gender=models.IntegerField(choices=GENDER_STATUS,verbose_name='性别')
    age=models.IntegerField(verbose_name='年龄')
    email=models.CharField(max_length=32,verbose_name='邮箱')
    def __str__(self):
        return self.name
    class Meta:
        db_table='author'
        verbose_name='作者'
        verbose_name_plural='作者'

class Type(models.Model):
    # id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name='类型名字')
    description=models.TextField(verbose_name='描述')
    def __str__(self):
        return self.name

    class Meta:
        db_table='type'
        verbose_name='文章类型'
        verbose_name_plural='文章类型'

class Article(models.Model):
    # id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=32,verbose_name='标题')
    date=models.DateField(auto_now=True,verbose_name='时间日期')
    content=RichTextField(verbose_name='文章内容')
    description=RichTextField(verbose_name='文章描述')

    # content=models.TextField(verbose_name='文章内容')
    # description=models.TextField(verbose_name='文章描述')
    picture=models.ImageField(upload_to='images',verbose_name='图片')
    recommend = models.IntegerField(default=0,verbose_name='推荐')
    cilck=models.IntegerField(default=0,verbose_name='点击率')
    author = models.ForeignKey(to=Author, to_field='id', on_delete=models.CASCADE)
    type=models.ManyToManyField(to=Type)
    def __str__(self):
        return self.title

    class Meta:
        db_table='article'
        verbose_name='文章表'
        verbose_name_plural='文章表'



class User(models.Model):
    username=models.CharField(max_length=32,verbose_name='用户名')
    password=models.CharField(max_length=32,verbose_name='密码')
    create_time=models.DateTimeField(auto_now=True,verbose_name='创建时间')

    class Meta:
        db_table='user'

