from django.db import models

from .user import User


class Todo(models.Model):
    user = models.ForeignKey(User)
    description = models.TextField('Описание', blank=False)
    is_done = models.BooleanField('Выполнено', default=False)
    created_at = models.DateTimeField('Дата создания', blank=False)
