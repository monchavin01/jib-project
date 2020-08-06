from django.test import TestCase

class TestWorkerListView(TestCase):
    def test_view_should_be_accessible(self):
        response  = self.client.get('/workers/')
        # print(dir(response))
        self.assertEqual(response.status_code, 200)
        