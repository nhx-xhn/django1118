# Generated by Django 2.2.1 on 2020-02-17 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20200217_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='时间日期'),
        ),
    ]
