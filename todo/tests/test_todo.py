from django.core.urlresolvers import reverse
from todo.tests import MainTestCase


class TodosTestCase(MainTestCase):

    def test_todo_list(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.get(
            reverse('todo_list')
        )

        self.assertEqual(200, response.status_code)

    def test_non_auth_todo_list(self):
        response = self.client.get(
            reverse('todo_list')
        )

        self.assertEqual(401, response.status_code)

    def test_insert_todo_item(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.post(
            reverse('insert_todo'),
            {
                'description': 'First todo'
            }
        )

        self.assertEqual(200, response.status_code)

    def test_non_auth_insert_todo_item(self):
        response = self.client.post(
            reverse('insert_todo'),
            {
                'description': 'First todo'
            }
        )

        self.assertEqual(401, response.status_code)

    def test_empty_description_insert_todo_item(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.post(
            reverse('insert_todo')
        )

        self.assertEqual(400, response.status_code)

    def test_update_todo_item(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.post(
            reverse('update_todo'),
            {
                'id': self.todo_1.id,
                'description': 'Update todo',
                'is_done': True
            }
        )

        self.assertEqual(200, response.status_code)

    def test_empty_id_update_todo_item(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.post(
            reverse('update_todo'),
            {
                'description': 'Update todo',
                'is_done': True
            }
        )

        self.assertEqual(400, response.status_code)

    def test_wrong_id_update_todo_item(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.post(
            reverse('update_todo'),
            {
                'id': 348765832,
                'description': 'Update todo',
                'is_done': True
            }
        )

        self.assertEqual(400, response.status_code)

    def test_delete_todo_item(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.post(
            reverse('delete_todo'),
            {
                'id': self.todo_1.id
            }
        )

        self.assertEqual(200, response.status_code)

    def test_non_auth_delete_todo_item(self):
        response = self.client.post(
            reverse('delete_todo'),
            {
                'id': self.todo_1.id
            }
        )

        self.assertEqual(401, response.status_code)

    def test_empty_id_delete_todo_item(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.post(
            reverse('delete_todo'),
        )

        self.assertEqual(400, response.status_code)

    def test_wrong_id_delete_todo_item(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.post(
            reverse('delete_todo'),
            {
                'id': 245432
            }
        )

        self.assertEqual(400, response.status_code)
