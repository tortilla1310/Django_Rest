from django.db import models
from uuid import uuid4


class Menus(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    home = models.CharField(max_length=64)
    contacts = models.CharField(max_length=64)
    service = models.CharField(max_length=64)
