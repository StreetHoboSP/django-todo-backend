from todo.tests import MainTestCase


class LoginTestCase(MainTestCase):

    def test_authorization(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

