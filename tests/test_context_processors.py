from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class ContextTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        self.client.force_authenticate(user)

    def test_mustachecp(self):
        """
        Ensure Mustache engine can pick up Django context processors
        """
        self.check_context_processor('/mustachecp')

    def test_djangocp(self):
        """
        Ensure Django engine can (still) pick up Django context processors
        """
        self.check_context_processor('/djangocp')

    def test_same_output(self):
        """
        Ensure analogous Mustache & Django templates produce the same output.
        """
        mustache_response = self.client.get('/mustachecp')
        django_response = self.client.get('/djangocp')
        mustache_html = mustache_response.content.decode('utf-8')
        django_html = django_response.content.decode('utf-8')
        self.assertHTMLEqual(
            mustache_html,
            django_html.replace(
                self.extract_token(django_html),
                self.extract_token(mustache_html),
            )
        )

    def check_context_processor(self, url):
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code), response.data)
        html = response.content.decode('utf-8')
        token = self.extract_token(html)
        expected_html = """
            <html>
                <p>conditional is true</p>
                <ul>
                  <li>1</li>
                  <li>2</li>
                  <li>3</li>
                </ul>
                <p>user is authenticated</p>
                <p>csrf is {csrf_token}</p>
                <p>username is testuser</p>
                <p>username is testuser</p>
            </html>
        """.format(csrf_token=token)
        self.assertHTMLEqual(expected_html, html)

    def extract_token(self, html):
        # As of Django 1.10, CSRF token is different on every request
        token = html.split('csrf is ')[1].split('<')[0]
        self.assertTrue(len(token) >= 32)
        return token
