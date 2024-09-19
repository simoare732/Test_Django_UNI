from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from books.models import Book
from .serializers import BookSerializer

class BookListAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer