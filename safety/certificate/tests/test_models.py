from django.test import TestCase
# from django.contrib import admin

from ..models import Certificate




class TestCertificate(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass




    def test_worker_should_have_defined_fields(self):
        # Given 
        name = 'Django Certificate by ODDS'
        issued_by = 'Proof'
      


        # When
        certificate = Certificate.objects.create(
            name = name,
            issued_by = issued_by,
         
        )

        # Then
        
        assert certificate.name == name
        assert certificate.issued_by == issued_by

    
