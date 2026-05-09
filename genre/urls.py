from django.urls import path
from genre.views import GenreCreateListView,GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('genre/', GenreCreateListView.as_view(), name='genre-list-create'),
    path('genre/<int:pk>', GenreRetrieveUpdateDestroyView.as_view(), name='genre-update-delete'),
]