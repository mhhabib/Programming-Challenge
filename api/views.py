from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .generate import RandomObjectGenerator
import json
# Create your views here.

class ApiView(views.APIView):
    def get(self, request):
        randomObject=RandomObjectGenerator().get_random_objects()
        randomObjectCount=RandomObjectGenerator().get_random_object_count()
        return Response({'randData':randomObject,'randCount': json.dumps(randomObjectCount)})
        