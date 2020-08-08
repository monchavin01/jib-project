from django.test import TestCase
from unittest.mock import patch
# Create your tests here.

class TestCovid19ReportView(TestCase):
    def test_view_should_be_accessible(self):
        response = self.client.get('/covid19-reports/')
        self.assertEqual(response.status_code, 200)

 # new add
    @patch('covid19_reports.views.requests.get')
    def test_view_should_call_covid19_api(self, mock):
        self.client.get('/covid19-reports/')
        mock.assert_called_once_with(
            'https://covid19.th-stat.com/api/open/today'
        )