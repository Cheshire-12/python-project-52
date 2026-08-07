from django.test import TestCase
from django.urls import reverse
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model

User = get_user_model()


class LabelsCRUDTestCase(TestCase):
    fixtures = ['users.json', 'labels.json']
    
    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.label = Label.objects.get(pk=2)

    def test_anonymous_access(self):
            urls = [
                reverse('labels:list'),
                reverse('labels:create'),
                reverse('labels:update', kwargs={'pk': self.label.pk}),
                reverse('labels:delete', kwargs={'pk': self.label.pk}),
            ]
            for url in urls:
                response = self.client.get(url)
                self.assertEqual(response.status_code, 302)

    def test_labels_list_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('labels:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bug')
        
    def test_label_pages_get(self):
        self.client.force_login(self.user)
        pages = [
            reverse('labels:create'),
            reverse('labels:update', kwargs={'pk': self.label.pk}),
            reverse('labels:delete', kwargs={'pk': self.label.pk}),
        ]
        for url in pages:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_label_success_create(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('labels:create'),
            {'name': 'Feature'}
        )
        self.assertRedirects(response, reverse('labels:list'))
        self.assertTrue(Label.objects.filter(name='Feature').exists())
    
    def test_label_create_duplicate_name(self):
            self.client.force_login(self.user)
            duplicate_data = {'name': self.label.name}
            response = self.client.post(
                reverse('labels:create'),
                data=duplicate_data
            )
            self.assertEqual(response.status_code, 200)
            self.assertFormError(response.context['form'], 'name', 'Label with this Name already exists.') # type: ignore

    def test_label_success_update(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('labels:update', kwargs={'pk': self.label.pk}),
            {'name': 'Critical Bug'}
        )
        self.assertRedirects(response, reverse('labels:list'))
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'Critical Bug')

    def test_label_success_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('labels:delete', kwargs={'pk': self.label.pk})
        )
        self.assertRedirects(response, reverse('labels:list'))
        self.assertFalse(Label.objects.filter(pk=self.label.pk).exists())