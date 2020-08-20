from django.contrib.auth.models import User,Group
from rest_framework import serializers

#序列化（自己创建的模块）
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:#原类
        model=User
        fields=("url","username","email","groups")

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=("url","name")

