# Generated by Django 4.1.7 on 2023-03-07 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangorestapp', '0002_users_usermail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uav',
            name='UavCategory',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='uav',
            name='UavModel',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='uav',
            name='UavName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='UserName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='UserPassword',
            field=models.CharField(max_length=50),
        ),
    ]