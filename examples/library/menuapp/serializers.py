from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Menus


class MenuModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Menus
        fields = '__all__'

