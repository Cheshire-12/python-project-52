from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class UserCRUDTestCase(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.user1 = User.objects.get(pk=1)
        
        self.user2 = User.objects.create_user(
            username='user2',
            password='password123',
            first_name='Alice',
            last_name='Smith'
        )

        self.new_user_data = {
            'username': 'new_user',
            'first_name': 'New',
            'last_name': 'User',
            'password1': 'strong_password_123',
            'password2': 'strong_password_123',
        }

    def test_user_list(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user1.username)
        self.assertContains(response, self.user2.username)

    def test_user_create_page(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)

    def test_user_create_success(self):
        response = self.client.post(reverse('user_create'),
                                    data=self.new_user_data)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='new_user').exists())

    def test_user_update_unauthenticated(self):
        url = reverse('user_update', kwargs={'pk': self.user1.pk})
        response = self.client.get(url)
        self.assertRedirects(response, reverse('users'))

    def test_user_update_self(self):
        self.client.force_login(self.user1)
        url = reverse('user_update', kwargs={'pk': self.user1.pk})
        
        updated_data = {
            'username': 'john_updated',
            'first_name': 'JohnUpdated',
            'last_name': 'DoeUpdated',
        }
        response = self.client.post(url, data=updated_data)
        self.assertRedirects(response, reverse('users'))
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.username, 'john_updated')

    def test_user_update_other_user(self):
        self.client.force_login(self.user1)
        url = reverse('user_update', kwargs={'pk': self.user2.pk})
        response = self.client.get(url)
        self.assertRedirects(response, reverse('users'))

    def test_user_delete_self(self):
        self.client.force_login(self.user2)
        url = reverse('user_delete', kwargs={'pk': self.user2.pk})
        response = self.client.post(url)
        self.assertRedirects(response, reverse('users'))
        self.assertFalse(User.objects.filter(pk=self.user2.pk).exists())

    def test_user_delete_other_user(self):
        self.client.force_login(self.user1)
        url = reverse('user_delete', kwargs={'pk': self.user2.pk})
        response = self.client.post(url)
        self.assertRedirects(response, reverse('users'))
        self.assertTrue(User.objects.filter(pk=self.user2.pk).exists())