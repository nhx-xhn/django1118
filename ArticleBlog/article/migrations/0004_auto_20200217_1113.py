# Generated by Django 2.2.1 on 2020-02-17 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200216_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='article.Author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.ManyToManyField(to='article.Type'),
        ),
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(choices=[(0, '女'), (1, '男')], max_length=32, verbose_name='性别'),
        ),
    ]
