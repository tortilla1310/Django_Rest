from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Users


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'uid',
            'username',
            'email',
            'firstname',
            'lastname',
            ]


class UserSerializerWithFullName(ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'username',
            'lastname',
        ]
        # fields = '__all__'
        # exclude = (
        #     'u_pass',
        #     'is_superuser',
        #     'is_staff',
        # )
        # read_only_fields = [
        #     'uid',
        #     'username',
        #     'firstname',
        #     'lastname',
        #     'email',
        # ]


class UserSerializerWithFullNameNew(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'username',
            'email',
            'firstname',
            'lastname',
            'is_superuser',
            'is_staff',
        )
