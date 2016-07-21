import django.test

from django.core.urlresolvers import reverse
from todo.models.user import User


class MainTestCase(django.test.TestCase):

    def setUp(self):
        self.client = django.test.Client()

        self.user_1 = User.objects.create(
            username='test',
        )
        self.user_1.set_password('test')
        self.user_1.save()

    def login(self, login='test', password='test'):
        response = self.client.post(
            reverse('login'),
            {
                'login': login,
                'password': password
            }
        )

        return response
