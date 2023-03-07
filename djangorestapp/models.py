from django.db import models

# Create your models here.
class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=50)
    UserMail = models.EmailField() 
    UserPassword = models.CharField(max_length=50)

class Uav(models.Model):
    UavId = models.AutoField(primary_key=True)
    UavName = models.CharField(max_length=50)
    UavModel = models.CharField(max_length=50)
    UavWeight = models.PositiveIntegerField()
    UavCategory = models.CharField(max_length=50)
