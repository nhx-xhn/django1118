# Generated by Django 2.2.1 on 2020-02-15 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_auto_20200214_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='num',
            field=models.IntegerField(default=11, verbose_name='数量'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=11, verbose_name='价格'),
            preserve_default=False,
        ),
    ]
