from rest_framework.viewsets import ModelViewSet
from .models import Footer
from .serializers import FooterModelSerializer


class FooterViewSet(ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterModelSerializer

