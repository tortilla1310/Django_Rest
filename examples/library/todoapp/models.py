from uuid import uuid4
from django.db import models
from usersapp.models import Users


class Project(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    name_project = models.CharField(verbose_name='Имя проекта', max_length=32)
    users = models.ManyToManyField(Users)


class TODO(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    text = models.TextField(verbose_name='Заметка')
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    update_at = models.DateField(verbose_name='Дата последнего обновления', auto_now=True)
    is_active = models.BooleanField(verbose_name='активация', default=True)
    project = models.ForeignKey(Project, verbose_name='uid проекта',
                                on_delete=models.PROTECT, null=True, related_name='project')

