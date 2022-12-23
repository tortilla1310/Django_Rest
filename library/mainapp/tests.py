import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIRequestFactory, force_authenticate, \
    APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from usersapp.models import Users
from usersapp.views import UserViewSet
from .views import AuthorModelViewSet
from .models import Author, Book, Biography, Article


class TestAuthorViewSet(TestCase):

    # def test_get_list(self):    # 1
    #     factory = APIRequestFactory()
    #     request = factory.get('/api/authors/')
    #     view = AuthorModelViewSet.as_view({'get': 'list'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_create_guest(self):    # 2
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/authors/', {
    #         'first_name': 'Александр',
    #         'last_name': 'Пушкин',
    #         'birthday_year': 1799
    #     }, format='json')
    #     view = AuthorModelViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #
    # def test_create_admin(self):    # 3
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/authors/', {
    #         'first_name': 'Александр',
    #         'last_name': 'Пушкин',
    #         'birthday_year': 1799
    #     }, format='json')
    #     admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
    #     force_authenticate(request, admin)
    #     view = AuthorModelViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    # def test_get_detail(self):    # 4
    #     author = Author.objects.create(
    #         first_name='Александр',
    #         last_name='Пушкин',
    #         birthday_year=1799
    #     )
    #     client = APIClient()
    #     response = client.get(f'/api/authors/{author.uid}/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #
    # def test_edit_guest(self):    # 5
    #     author = Author.objects.create(
    #         first_name='Александр',
    #         last_name='Пушкин',
    #         birthday_year=1799
    #     )
    #     client = APIClient()
    #     response = client.put(f'/api/authors/{author.uid}/', {
    #         'first_name': 'Александр',
    #         'last_name': 'Грин',
    #         'birthday_year': 1880
    #     })
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #
    # def test_edit_admin(self):    # 6
    #     author = Author.objects.create(
    #         first_name='Александр',
    #         last_name='Пушкин',
    #         birthday_year=1799
    #     )
    #     client = APIClient()
    #     admin = User.objects.create_superuser(
    #         'admin',
    #         'admin@admin.com',
    #         'admin')
    #     client.login(
    #         username='admin',
    #         password='admin'
    #     )
    #     response = client.put(f'/api/authors/{author.uid}/',
    #                           {
    #                               'first_name': 'Александр',
    #                               'last_name': 'Грин',
    #                               'birthday_year': 1880
    #                           })
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     author = Author.objects.get(uid=author.uid)
    #     self.assertEqual(author.last_name, 'Грин')
    #     self.assertEqual(author.birthday_year, 1880)
    #     client.logout()

    #     свои тесты
    def test_get_user_list(self):    # свой тест 1
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user(self):    # свой тест 2
        user = Users.objects.create(
            username='vano',
            firstname='Иван',
            lastname='Иванов',
            email='vano@drf.ru',
            u_pass='',
        )
        client = APIClient()
        response = client.get(f'/api/users/{user.uid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# class TestMath(APISimpleTestCase):
#     def test_sqrt(self):    # 7
#         import math
#         self.assertEqual(math.sqrt(4), 2)


# class TestBookViewSet(APITestCase):
#     def test_get_list(self):    # 8
#         response = self.client.get('/api/books/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_edit_admin(self):    # 9
    #     author = Author.objects.create(
    #         first_name='Александр',
    #         last_name='Пушкин',
    #         birthday_year=1799
    #     )
    #     book = Book.objects.create(
    #         name='Пиковая дама',
    #     )
    #     book.authors.add(author)
    #     book.save()
    #     admin = User.objects.create_superuser(
    #         'admin',
    #         'admin@admin.com',
    #         'admin'
    #     )
    #     self.client.login(
    #         username='admin',
    #         password='admin'
    #     )
    #     response = self.client.put(f'/api/books/{book.id}/',
    #                                {
    #                                    'name': 'Руслан и Людмила',
    #                                    'authors': author.uid
    #                                })
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     book = Book.objects.get(pk=book.id)
    #     self.assertEqual(book.name, 'Руслан и Людмила')

    # def test_edit_mixer(self):    # 10
    #     book = mixer.blend(Book)
    #     admin = User.objects.create_superuser(
    #         'admin',
    #         'admin@admin.com',
    #         'admin'
    #     )
    #     self.client.login(
    #         username='admin',
    #         password='admin'
    #     )
    #     response = self.client.put(f'/api/books/{book.id}/',
    #                                {
    #                                    'name': 'Руслан и Людмила',
    #                                    'authors': book.authors
    #                                })
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     book = Book.objects.get(pk=book.id)
    #     self.assertEqual(book.name, 'Руслан и Людмила')

    # def test_get_detail(self):    # 11
    #     book = mixer.blend(Book, name='Алые паруса')
    #     response = self.client.get(f'/api/books/{book.id}/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     response_book = json.loads(response.content)
    #     self.assertEqual(response_book['name'], 'Алые паруса')

    # def test_get_detail_author(self):    # 12
    #     book = mixer.blend(Book, authors__last_name='Грин')
    #     response = self.client.get(f'/api/books/{book.id}/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     response_book = json.loads(response.content)
    #     self.assertEqual(response_book['authors']['last_name'], 'Грин')

# свои тесты
class TestUserViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):    # свой тест 3
        author = Author.objects.create(
            first_name='Александр',
            last_name='Грин',
            birthday_year=1800
        )
        article = Article.objects.create(
            name='и жили они долго, но не счастливо',
            authors=author
        )

        admin = User.objects.create_superuser(
            'admin',
            'admin@admin.com',
            'admin'
        )
        self.client.login(
            username='admin',
            password='admin'
        )
        response = self.client.put(f'/api/article/{article.id}/',
                                   {
                                       'name': 'неизвестные факты',
                                       'authors': article.authors.uid
                                   })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        article = Article.objects.get(pk=article.id)
        self.assertEqual(article.name, 'неизвестные факты')


