from rest_framework import serializers


class HelloWorldSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=6)
    age = serializers.IntegerField(required=False, max_value=10, default=10)