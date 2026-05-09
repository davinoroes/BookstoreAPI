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
