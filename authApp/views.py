from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.


def hello_world():
    return JsonResponse({"message": "hello world!"})
