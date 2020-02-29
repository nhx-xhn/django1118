from django.db import models

# Create your models here.
GENDER=(
    (0,'女'),
    (1,'男'),
)

class Author(models.Model):
    # id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name='作者名字')
    # gender=models.CharField(max_length=32,verbose_name='性别')
    gender=models.IntegerField(choices=GENDER,max_length=32,verbose_name='性别')
    age=models.IntegerField(verbose_name='年龄')
    email=models.CharField(max_length=32,verbose_name='邮箱')
    class Meta:
        db_table='author'
        verbose_name='作者'
        verbose_name_plural='作者'

class Type(models.Model):
    # id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name='类型名字')
    description=models.TextField(verbose_name='描述')

    class Meta:
        db_table='type'
        verbose_name='文章类型'
        verbose_name_plural='文章类型'

class Article(models.Model):
    # id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=32,verbose_name='标题')
    date=models.DateField(verbose_name='时间日期')
    content=models.TextField(verbose_name='文章内容')
    description=models.TextField(verbose_name='文章描述')
    author = models.ForeignKey(to=Author, to_field='id', on_delete=models.CASCADE)
    type=models.ManyToManyField(to=Type)

    class Meta:
        db_table='article'
        verbose_name='文章表'
        verbose_name_plural='文章表'







