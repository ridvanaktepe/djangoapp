from rest_framework import serializers
from djangorestapp.models import Uav, Users

class UavSerializer(serializers.ModelSerializer):
    class Meta:
        model=Uav
        fields=('UavId','UavName','UavModel','UavWeight','UavCategory')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields=('UserId','UserName','UserPassword')
    


