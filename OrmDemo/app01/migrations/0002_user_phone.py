# Generated by Django 2.2.1 on 2020-02-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='1', max_length=11),
            preserve_default=False,
        ),
    ]
