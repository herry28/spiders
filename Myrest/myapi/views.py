from django.shortcuts import render
from django.contrib.auth.models import User,Group
from  rest_framework import viewsets
from myapi.serializers import UserSerializer,GroupSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    retrive:
    Return a user instance.
    list:
    Return all users,odered by most recent joined
    create:
    create a new user.
    delete:
    remove a existing user.
    partial_update:
    update one or more fields on an existing group.
    update:
    update a user

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    """
        retrive:
        Return a group instance.
        list:
        Return all groups,odered by most recent joined
        create:
        create a new group.
        delete:
        remove a existing group.
        partial_update:
        update one or more fields on an existing group.
        update:
        update a group

        """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
