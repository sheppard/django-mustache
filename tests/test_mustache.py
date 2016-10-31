from rest_framework.test import APITestCase
from rest_framework import status


class MustacheTestCase(APITestCase):
    def test_context(self):
        """
        Ensure basic Mustache context operations work as expected.
        """
        self.check_html(
            '/context',
            """
            <html>
              <h1>1234</h1>
              <p>conditional is true</p>
              <p>None is ""</p>
              <p>conditional is false</p>
              <p>nested value is 5678</p>
              <p>nested value is 5678</p>
              <p>missing value is missing</p>
              <ul>
                <li>1</li>
                <li>2</li>
                <li>3</li>
              </ul>
              <p>empty list</p>
            </html>
            """
        )

    def test_partials(self):
        """
        Ensure including a Mustache partial template works as expected.
        """
        self.check_html(
            '/partials',
            """
            <html>
              <p>partial template content</p>
            </html>
            """
        )

    def test_app_dirs(self):
        self.check_html(
            '/apptemplate',
            """
            <html>
              <p>test</p>
            </html>
            """
        )

    def check_html(self, url, expected_html):
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code), response.data)
        html = response.content.decode('utf-8')
        self.assertHTMLEqual(expected_html, html)
