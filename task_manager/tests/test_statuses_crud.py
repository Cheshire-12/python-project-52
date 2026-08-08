from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status

User = get_user_model()


class StatusCRUDTestCase(TestCase):
    fixtures = ['users.json', 'statuses.json']

    def setUp(self):
        self.user1 = User.objects.get(pk=1)
        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.create(name='In Progress')

        self.new_status_data = {
            'name': 'New Status',
        }

    def test_anonymous_access(self):
        urls = [
            reverse('statuses:list'),
            reverse('statuses:create'),
            reverse('statuses:update', kwargs={'pk': self.status1.pk}),
            reverse('statuses:delete', kwargs={'pk': self.status1.pk}),
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)

    def test_status_list(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('statuses:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.status1.name)
        self.assertContains(response, self.status2.name)

    def test_status_pages_get(self):
        self.client.force_login(self.user1)
        pages = [
            reverse('statuses:create'),
            reverse('statuses:update', kwargs={'pk': self.status1.pk}),
            reverse('statuses:delete', kwargs={'pk': self.status1.pk}),
        ]
        for url in pages:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_status_success_create(self):
        self.client.force_login(self.user1)
        response = self.client.post(
            reverse('statuses:create'),
            data=self.new_status_data
        )
        self.assertRedirects(response, reverse('statuses:list'))
        self.assertTrue(Status.objects.filter(name='New Status').exists())

    def test_status_create_duplicate_name(self):
        self.client.force_login(self.user1)
        duplicate_data = {'name': self.status1.name}
        response = self.client.post(
            reverse('statuses:create'),
            data=duplicate_data
        )
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response.context['form'],
                            'name',
                            'Status with this Name already exists.')  # type: ignore

    def test_status_success_update(self):
        self.client.force_login(self.user1)
        updated_data = {'name': 'Updated Status'}
        response = self.client.post(
            reverse('statuses:update', kwargs={'pk': self.status1.pk}),
            data=updated_data
        )
        self.assertRedirects(response, reverse('statuses:list'))
        self.status1.refresh_from_db()
        self.assertEqual(self.status1.name, 'Updated Status')

    def test_status_success_delete(self):
        self.client.force_login(self.user1)
        response = self.client.post(
            reverse('statuses:delete', kwargs={'pk': self.status1.pk})
        )
        self.assertRedirects(response, reverse('statuses:list'))
        self.assertFalse(Status.objects.filter(pk=self.status1.pk).exists())