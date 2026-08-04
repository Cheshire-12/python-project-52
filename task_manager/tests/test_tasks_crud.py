from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from task_manager.tasks.models import Task

User = get_user_model()


class TaskCRUDTestCase(TestCase):
    fixtures = ['tasks.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.task = Task.objects.get(pk=1)
        self.new_task_data = {
            'name': 'New Task',
            'description': 'This is a new task.',
            'status': self.task.status.pk,
            'executor': self.user.pk,
        }

    def test_anonymous_access(self):
        urls = [
            reverse('tasks:list'),
            reverse('tasks:create'),
            reverse('tasks:detail', kwargs={'pk': self.task.pk}),
            reverse('tasks:update', kwargs={'pk': self.task.pk}),
            reverse('tasks:delete', kwargs={'pk': self.task.pk}),
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)

    def test_task_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('tasks:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.name)

    def test_task_pages_get(self):
        self.client.force_login(self.user)
        pages = [
            reverse('tasks:create'),
            reverse('tasks:detail', kwargs={'pk': self.task.pk}),
            reverse('tasks:update', kwargs={'pk': self.task.pk}),
            reverse('tasks:delete', kwargs={'pk': self.task.pk}),
        ]
        for url in pages:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_task_create_success(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('tasks:create'),
            data=self.new_task_data
        )
        self.assertRedirects(response, reverse('tasks:list'))
        
        created_task = Task.objects.get(name='New Task')
        self.assertIsNotNone(created_task)
        self.assertEqual(created_task.author, self.user)

    def test_task_detail_view(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('tasks:detail', kwargs={'pk': self.task.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.name)
        self.assertContains(response, self.task.description)

    def test_task_update(self):
        self.client.force_login(self.user)
        updated_data = {
            'name': 'Updated Task Name',
            'description': self.task.description,
            'status': self.task.status.pk,
            'executor': self.user.pk,
        }
        response = self.client.post(
            reverse('tasks:update', kwargs={'pk': self.task.pk}),
            data=updated_data
        )
        self.assertRedirects(response, reverse('tasks:list'))
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, 'Updated Task Name')

    def test_task_delete_by_author(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('tasks:delete', kwargs={'pk': self.task.pk})
        )
        self.assertRedirects(response, reverse('tasks:list'))
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_task_delete_by_non_author(self):
        other_user = User.objects.create_user(
            username='other_user',
            password='password123'
        )
        self.client.force_login(other_user)
        response = self.client.post(
            reverse('tasks:delete', kwargs={'pk': self.task.pk})
        )
        self.assertRedirects(response, reverse('tasks:list'))
        self.assertTrue(Task.objects.filter(pk=self.task.pk).exists())