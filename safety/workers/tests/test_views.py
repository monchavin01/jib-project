from django.test import TestCase
from ..models import Worker
import json


class TestWorkerListView(TestCase):
    def test_view_should_be_accessible(self):
        response  = self.client.get('/workers/')
        # print(dir(response))
        self.assertEqual(response.status_code, 200)
        
    def test_view_should_render_list_of_worker_name(self):
        #Given
        Worker.objects.create(
            first_name = 'keng',
            last_name = 'mak',
            is_available = True,
            primary_phone = '081-689-777x',
            secondary_phone = '081-689-777x',
            address = 'Geeky Base All Stars',
        )
        Worker.objects.create(
            first_name = 'oh',
            last_name = 'hoooo',
            is_available = True,
            primary_phone = '081-689-555x',
            secondary_phone = '081-689-555x',
            address = 'Geeky Extreame Survivor',
        )


        # When
        response = self.client.get('/workers/')

        # Then 
        #self.assertContains(response, '<li>keng</li>')
        #self.assertContains(response, '<li>oh</li>')

        expected = [
            {
                'name': 'keng'
            },
            {
                'name': 'oh'
            }
        ]

        self.assertEqual(
            response.content.decode('utf-8'), 
            json.dumps(expected)
            )