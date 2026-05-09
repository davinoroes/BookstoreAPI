from django.shortcuts import render
from rest_framework import generics
from genre.models import Genre
from genre.serializers import GenreModelSerializer

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer

    def get(self, request, *args, **kwargs):
        print(f'Listando generos - Metodo: {request.method} - Path: {request.path}')
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        print(f'Criando genero - Metodo: {request.method} - Path: {request.path} - Genero: {request.data}')
        return super().post(request, *args, **kwargs)
    


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer

    def get(self, request, *args, **kwargs):
        print(f'listando genero especifico - {request.data}')
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        print(f'editando genero especifico - id({kwargs.get('pk')})')
        return super().put(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        print(f'deletando genero especifico - id({kwargs.get('pk')})')
        return super().delete(request, *args, **kwargs)