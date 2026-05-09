from django.shortcuts import render
from rest_framework import generics
from writer.models import Writer
from writer.serializers import WriterSerializer

class WriterListCreateView(generics.ListCreateAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

    def get(self, request, *args, **kwargs):
        print(f'listando escritores - Metodo: {request.method} - Path: {request.path}')
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        print(f'criando escritor - Metodo: {request.method} - Path: {request.path} - Genero: {request.data}')
        return super().post(request, *args, **kwargs)
class WriterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

    def get(self, request, *args, **kwargs):
        print(f'listando escritor especifico')
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        print(f'editando escritor especifico - id({kwargs.get('pk')})')
        return super().put(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        print(f'deletando escritor especifico - id({kwargs.get('pk')})')
        return super().delete(request, *args, **kwargs)

