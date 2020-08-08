from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Certificate
from.serializers import CertificateModelSerializer
# Create your views here.

class CertificateModelViewSetView(ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateModelSerializer