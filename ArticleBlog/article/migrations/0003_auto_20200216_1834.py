# Generated by Django 2.2.1 on 2020-02-16 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200215_1219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章表', 'verbose_name_plural': '文章表'},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': '文章类型', 'verbose_name_plural': '文章类型'},
        ),
        migrations.RemoveField(
            model_name='type',
            name='article',
        ),
        migrations.AddField(
            model_name='type',
            name='article',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='article.Article'),
            preserve_default=False,
        ),
    ]
