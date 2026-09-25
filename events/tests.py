from django.test import TestCase, Client
from django.urls import reverse


class EventPlannerTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page_ok(self):
        response = self.client.get(reverse('events:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Мои события')

    def test_settings_page_ok(self):
        response = self.client.get(reverse('events:settings'))
        self.assertEqual(response.status_code, 200)

    def test_settings_save_cookies(self):
        response = self.client.post(reverse('events:settings'), {
            'theme': 'dark',
            'language': 'en',
            'notification_email': 'test@example.com',
            'notify_before': '60',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.cookies['theme'].value, 'dark')
        self.assertEqual(response.cookies['language'].value, 'en')

    def test_add_event_form(self):
        response = self.client.post(reverse('events:add_event'), {
            'title': 'Тест',
            'date': '2025-05-01',
            'time': '12:00',
            'category': 'work',
            'description': 'Описание',
            'notify': True,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тест')
