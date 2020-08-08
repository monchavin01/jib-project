from django.test import TestCase

# Create your tests here.

class TestCovid19ReportView(TestCase):
    def test_view_should_be_accessible(self):
        response = self.client.get('/covid19-reports/')
        self.assertEqual(response.status_code, 200)