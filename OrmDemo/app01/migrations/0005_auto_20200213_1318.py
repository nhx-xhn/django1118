# Generated by Django 2.2.1 on 2020-02-13 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20200213_1202'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='user_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
