from rest_framework.viewsets import ModelViewSet
from .models import Menus
from .serializers import MenuModelSerializer


class MenuViewSet(ModelViewSet):
    queryset = Menus.objects.all()
    serializer_class = MenuModelSerializer
