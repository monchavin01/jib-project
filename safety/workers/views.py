import json

from rest_framework.response import Response
from rest_framework import serializers, viewsets
from rest_framework.views import APIView


from .models import Worker


# class-base view

class WorkerSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=40)
    is_available = serializers.BooleanField()
    primary_phone = serializers.CharField(max_length=10)
    secondary_phone = serializers.CharField(max_length=10)
    address = serializers.CharField()


class WorkerListView(APIView):
    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)


class WorkerModelViewSetView(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer