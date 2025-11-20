from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Todo


class TodoModelTests(TestCase):
    def test_create_todo_with_due_date(self):
        due = date(2025, 1, 31)
        todo = Todo.objects.create(
            title="Test task",
            description="Test description",
            due_date=due,
        )
        self.assertEqual(todo.title, "Test task")
        self.assertEqual(todo.due_date, due)
        self.assertFalse(todo.is_completed)


class TodoViewTests(TestCase):
    def test_create_todo_via_post(self):
        url = reverse("todo_list")
        resp = self.client.post(url, {
            "action": "create",
            "title": "Task from POST",
            "description": "Created via view",
            "due_date": "2025-02-01",
        })
        self.assertEqual(resp.status_code, 302)  # redirect
        self.assertEqual(Todo.objects.count(), 1)
        todo = Todo.objects.first()
        self.assertEqual(todo.title, "Task from POST")
        self.assertEqual(todo.due_date, date(2025, 2, 1))

    def test_toggle_completion(self):
        todo = Todo.objects.create(title="Toggle me")
        url = reverse("todo_list")

        resp = self.client.post(url, {
            "action": "toggle",
            "todo_id": todo.id,
        })
        self.assertEqual(resp.status_code, 302)
        todo.refresh_from_db()
        self.assertTrue(todo.is_completed)

        resp = self.client.post(url, {
            "action": "toggle",
            "todo_id": todo.id,
        })
        self.assertEqual(resp.status_code, 302)
        todo.refresh_from_db()
        self.assertFalse(todo.is_completed)

    def test_delete_todo(self):
        todo = Todo.objects.create(title="Delete me")
        url = reverse("todo_list")

        resp = self.client.post(url, {
            "action": "delete",
            "todo_id": todo.id,
        })
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Todo.objects.count(), 0)

    def test_edit_todo(self):
        todo = Todo.objects.create(
            title="Old title",
            description="Old description",
        )
        url = reverse("edit_todo", args=[todo.id])

        resp = self.client.post(url, {
            "title": "New title",
            "description": "New description",
            "due_date": "2025-03-10",
        })
        self.assertEqual(resp.status_code, 302)

        todo.refresh_from_db()
        self.assertEqual(todo.title, "New title")
        self.assertEqual(todo.description, "New description")
        self.assertEqual(todo.due_date, date(2025, 3, 10))
