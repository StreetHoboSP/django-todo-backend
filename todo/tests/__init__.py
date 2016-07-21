import django.test

from datetime import datetime
from django.core.urlresolvers import reverse
from todo.models.todo import Todo
from todo.models.user import User


class MainTestCase(django.test.TestCase):

    def setUp(self):
        self.client = django.test.Client()

        self.user_1 = User.objects.create(
            username='test',
        )
        self.user_1.set_password('test')
        self.user_1.save()

        self.todo_1 = Todo.objects.create(
            user=self.user_1,
            is_done=False,
            description='descrp',
            created_at=datetime.now()
        )

    def login(self, login='test', password='test'):
        response = self.client.post(
            reverse('login'),
            {
                'login': login,
                'password': password
            }
        )

        return response
