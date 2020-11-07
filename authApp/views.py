from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class HelloWorldView(APIView):
    def get(self, request):
        return Response({'message': 'Hello World!'})

    def post(self, request):
        name = request.data.get("name")
        if not name:
            return Response({"error": "No name passed"})
        return Response({"message": "Hello {}!".format(name)})
