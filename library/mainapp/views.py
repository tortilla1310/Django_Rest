from rest_framework import viewsets, permissions
# from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.permissions import AllowAny
# from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Biography, Article
from .serializers import AuthorModelSerializer, BookModelSerializer, BiographyModelSerializer, ArticleModelSerializer, \
    BookSerializerBase, AuthorSerializerBase
from .serializers import BookSerializerBase


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return AuthorSerializerBase
        return AuthorModelSerializer


class BookModelViewSet(ModelViewSet):
    # permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BookModelSerializer
        return BookSerializerBase


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class ArticleKwargsFilterView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')

        articles = Article.objects.all()
        if name:
            articles = articles.filter(name__contains=name)
        return articles


class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class ArticleLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    pagination_class = ArticleLimitOffsetPagination
