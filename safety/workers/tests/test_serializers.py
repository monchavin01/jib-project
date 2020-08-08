from django.test import TestCase
from ..models import Worker
from ..serializers import WorkerSerializer

class TestWorkSerializer(TestCase):
    def test_serializer_should_return_data_correct_serializer_data(self):
        worker = Worker.objects.create(
            first_name = 'golf',
            last_name = 'pinthong',
            is_available = True,
            primary_phone = '0899999999',
            secondary_phone = '06777777',
            address = 'Odds',

        )
        serializer = WorkerSerializer(worker)

        expected = {
            'first_name': 'golf',
            'last_name': 'pinthong',
            'is_available' : True,
            'primary_phone': '0899999999',
            'secondary_phone': '06777777',
            'address': 'Odds',
        }
        assert serializer.data == expected