
from django.test import TestCase

from ..views import CertificateModelViewSetView
from ..models import Certificate
from ..serializers import CertificateModelSerializer




class TestCertificateModelViewSetView(TestCase):
    def test_model_view_set_should_set_queryset(self):
        assert list(CertificateModelViewSetView.queryset) == list(Certificate.objects.all())
       
        
    def test_model_view_set_should_set_serialzer_class(self):
        assert CertificateModelViewSetView.serializer_class == CertificateModelSerializer
       