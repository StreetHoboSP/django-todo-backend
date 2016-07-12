import django.test

from django.core.urlresolvers import reverse
from todo.models import User


class LoginTestCase(django.test.TestCase):

    def setUp(self):
        self.user_1 = User.objects.create(
            username='test',
        )

        self.user_1.set_password('test')
        self.user_1.save()

    def test_authorization(self):
        client = django.test.Client()

        response = client.post(
            reverse('login'),
            {
                'login': 'test',
                'password': 'test'
            }
        )

        self.assertEqual(200, response.status_code)
