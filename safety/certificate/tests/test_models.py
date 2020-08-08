from django.test import TestCase
# from django.contrib import admin

from ..models import Certificate
from workers.models import Worker



class TestCertificate(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass




    def test_worker_should_have_defined_fields(self):


        worker = Worker.objects.create(
            first_name = 'keng',
            last_name = 'mak',
            is_available = True,
            primary_phone = '081-689-777x',
            secondary_phone = '081-689-777x',
            address = 'Geeky Base All Stars',
        )
        
        name = 'Django Certificate byODDS'
        issued_by = 'Proof'
      


        # When
        certificate = Certificate.objects.create(
            name = name,
            issued_by = issued_by,
            worker = worker,
         
        )

        # Then
        
        assert certificate.name == name
        assert certificate.issued_by == issued_by
        assert certificate.worker.first_name == worker.first_name

    
