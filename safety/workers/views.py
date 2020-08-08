import json

from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
#from rest_framework import viewsets

from .models import Worker


# class-base view

from .serializers import WorkerSerializer

class WorkerListView(APIView):
    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)


#class WorkerModelViewSetView(viewsets.ModelViewSet):
#    queryset = Worker.objects.all()
 #   serializer_class = WorkerSerializer

 #   def create(self, request):
 #       print(request.data)
 #       return Response()