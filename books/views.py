from django.db.models import Q
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Book
from .serializers import BookCreateSerializer, BookListSerializer


class BookListAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookListSerializer

    def post(self, request, *args, **kwargs):
        branch = request.data['branch']
        college = request.data['college']
        semester = request.data['semester']
        books = Book.objects.filter(
            Q(branch__iexact=branch) &
            Q(owner__college__iexact=college) &
            Q(semester=semester)
        )
        return Response({
            "books": BookListSerializer(books, many=True).data
        })


class BookCreateAPIView(generics.GenericAPIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]
    serializer_class = BookCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response('Book created successfully')


class CreatedBooksAPIView(generics.ListAPIView):
    serializer_class = BookListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        books = self.request.user.books.all()
        return books
