# Generated by Django 2.2.1 on 2020-02-13 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20200213_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='出版社名字')),
                ('address', models.CharField(max_length=32, verbose_name='出版社地址')),
            ],
            options={
                'db_table': 'publish',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='书名')),
                ('publish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publish')),
            ],
        ),
    ]
