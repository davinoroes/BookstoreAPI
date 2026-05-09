from django.urls import path
from books.views import BookCreateListView,BookRetrieveUpdateDestroyView

urlpatterns = [
    path('book/',BookCreateListView.as_view(), name='book-list-create' ),
    path('book/<int:pk>', BookRetrieveUpdateDestroyView.as_view(),name='book-update-delete'),
]