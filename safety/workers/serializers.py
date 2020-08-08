from rest_framework import serializers

class WorkerSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=40)
    is_available = serializers.BooleanField()
    primary_phone = serializers.CharField(max_length=10)
    secondary_phone = serializers.CharField(max_length=10)
    address = serializers.CharField()
