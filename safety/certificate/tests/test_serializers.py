from django.test import TestCase

from ..serializers import CertificateModelSerializer
from ..models import Certificate

class TestCertificateModelSerializer(TestCase):
    def test_model_serializer_should_set_certificate_model(self):
        assert CertificateModelSerializer.Meta.model == Certificate

    def test_model_serializer_should_use_all_fields(self):
        assert CertificateModelSerializer.Meta.fields == Certificate

