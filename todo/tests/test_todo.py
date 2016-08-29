import json

from django.core.urlresolvers import reverse
from todo.tests import MainTestCase


class TodosTestCase(MainTestCase):

    def test_todo_list(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.get(
            reverse('todos')
        )

        self.assertEqual(200, response.status_code)

    def test_non_auth_todo_list(self):
        response = self.client.get(
            reverse('todos')
        )

        self.assertEqual(401, response.status_code)

    def test_insert_todo_item(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.post(
            reverse('todos'),
            data=json.dumps({
                'description': 'First todo'
            }),
            content_type='application/json',
        )

        self.assertEqual(200, response.status_code)

    def test_non_auth_insert_todo_item(self):
        response = self.client.post(
            reverse('todos'),
            data=json.dumps({
                'description': 'First todo'
            }),
            content_type='application/json',
        )

        self.assertEqual(401, response.status_code)

    def test_empty_description_insert_todo_item(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.post(
            reverse('todos')
        )

        self.assertEqual(400, response.status_code)

    def test_update_todo_item(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.put(
            reverse('todo_item', kwargs=dict(id=self.todo_1.id)),
            data=json.dumps({
                'description': 'Update todo',
                'is_done': True
            }),
            content_type='application/json',
        )

        self.assertEqual(200, response.status_code)

    def test_wrong_id_update_todo_item(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.put(
            reverse('todo_item', kwargs=dict(id=self.wrond_id)),
            data=json.dumps({
                'description': 'Update todo',
                'is_done': True
            }),
            content_type='application/json',
        )

        self.assertEqual(400, response.status_code)

    def test_delete_todo_item(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.delete(
            reverse('todo_item', kwargs=dict(id=self.todo_1.id)),
        )

        self.assertEqual(200, response.status_code)

    def test_non_auth_delete_todo_item(self):
        response = self.client.delete(
            reverse('todo_item', kwargs=dict(id=self.todo_1.id)),
        )

        self.assertEqual(401, response.status_code)

    def test_wrong_id_delete_todo_item(self):
        response = self.login()

        self.assertEqual(200, response.status_code)

        response = self.client.delete(
            reverse('todo_item', kwargs=dict(id=self.wrond_id)),
        )

        self.assertEqual(400, response.status_code)
