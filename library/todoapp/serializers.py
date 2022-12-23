from rest_framework import serializers, request
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from mainapp.serializers import AuthorModelSerializer
from usersapp import models
from usersapp.models import Users
from usersapp.serializers import UserSerializerWithFullName, UserModelSerializer, UserSerializerWithFullNameNew
from .models import Project, TODO


class ProjectModelSerializer(ModelSerializer):    # HyperlinkedModelSerializer
    users = UserModelSerializer

    class Meta:
        model = Project
        fields = '__all__'


class TODOModelSerializer(ModelSerializer):    # HyperlinkedModelSerializer
    project = ProjectModelSerializer

    class Meta:
        model = TODO
        fields = '__all__'
