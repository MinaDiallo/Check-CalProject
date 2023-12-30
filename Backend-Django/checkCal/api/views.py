from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from . models import *

# Create your views here.
class FoodsView(generics.ListAPIView): #ListAPIView
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer
    
class CreateFoodsView(APIView):
    def post(self, request, format =None):
        serializer = CreateFoodsSerializer(data= request.data)
        if serializer.is_valid(raise_exception =True):
            serializer.save()
            return Response(serializer.data)