from django.shortcuts import render
from rest_framework import generics
from writer.models import Writer
from writer.serializers import WriterSerializer

class WriterListCreateView(generics.ListCreateAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

class WriterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

