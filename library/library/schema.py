import graphene
from graphene_django import DjangoObjectType
from mainapp.models import Book, Author
from todoapp.models import Project, TODO
from usersapp.models import Users


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = 'id', 'name'
        # если использовать '__all__', будет ошибка повторяющихся данных (для all_authors)
        # так как таблицы имеют связи многие ко многим ('id', 'name')


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


# для ДЗ-10
class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


# для ДЗ-10
class TODOType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


# для ДЗ-10
class UsersType(DjangoObjectType):
    class Meta:
        model = Users
        fields = '__all__'


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)  # лучше вырубить временно
    author_by_uid = graphene.Field(AuthorType, uid=graphene.String(required=True))  # вместо Int пишем String,
    # так как вместо id в БД используется uid (в нём используются не только цифры)
    books_by_author_name = graphene.List(BookType, name=graphene.String(required=False))
    # напишу для ДЗ-10
    all_todo = graphene.List(TODOType)

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_all_authors(root, info):
        return Author.objects.all()

    def resolve_author_by_uid(self, info, uid):
        try:
            return Author.objects.get(uid=uid)  # тут не забываем указать uid для запроса (везде, вместо id)
        except Author.DoesNotExist:
            return None
        # в форме (в браузере) запросы на uid писать в кавычках! нпр, "b30f3654-bf21-4d1a-8d45-e07d51ffdd9b"

    def resolve_books_by_author_name(self, info, name=None):
        books = Book.objects.all()
        if name:
            books = books.filter(authors__last_name=name)
        return books

    # для ДЗ-10
    def resolve_all_todo(root, info):
        return TODO.objects.all()

    # этот запрос для ДЗ-10 точно работает ))
    # {
    #     allTodo {
    #         text
    #         updateAt
    #         project {
    #             nameProject
    #             users {
    #                 username
    #             }
    #         }
    #     }
    # }


class AuthorMutation(graphene.Mutation):    # по аналогии uid писать в кавычках при запросе

    class Arguments:
        birthday_year = graphene.Int(required=True)
        uid = graphene.ID()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, birthday_year, uid):
        author = Author.objects.get(pk=uid)
        author.birthday_year = birthday_year
        author.save()
        return AuthorMutation(author=author)


class Mutation(graphene.ObjectType):
    update_author = AuthorMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
