from rest_framework.serializers import ModelSerializer
from .models import Certificate


class CertificateModelSerializer(ModelSerializer):

    class Meta:
        model = Certificate
        firlds = '__all__'