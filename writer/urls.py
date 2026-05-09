from django.urls import path
from writer.views import WriterListCreateView,WriterRetrieveUpdateDestroyView

urlpatterns = [
    path('writer/', WriterListCreateView.as_view(), name='writer-list-create'),
    path('writer/<int:pk>',WriterRetrieveUpdateDestroyView.as_view(), name='writer-update-delete'),
]