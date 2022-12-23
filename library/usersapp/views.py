from django.http import Http404
from rest_framework import status, generics
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Users
from .serializers import UserModelSerializer, UserSerializerWithFullName, UserSerializerWithFullNameNew


class UserViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserModelSerializer


class UsersList(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self):
        queryset = Users.objects.all()
        serializer = UserModelSerializer(queryset, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self, uid):
        try:
            return Users.objects.get(pk=uid)
        except Exception:
            raise Http404

    def get(self, uid):
        queryset = self.get_object(uid)
        serializer = UserModelSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, uid):
        queryset = self.get_object(uid)

        serializer = UserModelSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserSerializerWithFullNameNew    # отсылка к новому сериализатору.('is_superuser','is_staff',)
        return UserModelSerializer    # а вот этот сериализатор старый, без ('is_superuser','is_staff',)
