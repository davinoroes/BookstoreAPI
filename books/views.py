from django.shortcuts import render
from rest_framework import generics
from books.models import Book
from books.serializers import BookSerializer

class BookCreateListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
            print(f'listando livros - Metodo: {request.method} - Path: {request.path}')
            return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        print(f'criando livro - Metodo: {request.method} - Path: {request.path} - Genero: {request.data}')
        return super().post(request, *args, **kwargs)

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        print(f'listando genero especifico')
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        print(f'editando genero especifico - id({kwargs.get('pk')})')
        return super().put(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        print(f'deletando genero especifico - id({kwargs.get('pk')})')
        return super().delete(request, *args, **kwargs)
