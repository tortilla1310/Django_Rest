from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from .models import Project, TODO
from .serializers import ProjectModelSerializer, TODOModelSerializer


class ProjectLimitPagination(LimitOffsetPagination):
    default_limit = 100
    max_limit = 100


class ProjectLimitPaginatonViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitPagination


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

    def get_queryset(self):
        param = self.request.query_params.get('title')
        if param is not None:
            return Project.objects.filter(title__contains=param)
        return super().get_queryset()


class TodoLimitPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoLimitPaginatonListCreate(generics.ListCreateAPIView):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    pagination_class = TodoLimitPagination


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer

    def get_queryset(self):
        param = self.request.query_params.get('name')
        if param is not None:
            return Project.objects.filter(name__contains=param)
        return super().get_queryset()
