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
        self.assertHTMLEqual(
            mustache_response.content.decode('utf-8'),
            django_response.content.decode('utf-8'),
        )

    def check_context_processor(self, url):
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code), response.data)
        token = response.cookies['csrftoken'].value
        html = response.content.decode('utf-8')
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
