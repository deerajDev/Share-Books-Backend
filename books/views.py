from django.db.models import Q
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from accounts.models import College
from .models import Book
from .serializers import BookCreateSerializer, BookListSerializer, CollegeListSerializer
from .pagination import BookListPaginator


class BookListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookListSerializer
    pagination_class = BookListPaginator

    def get_queryset(self, *args, **kwargs):
        branch = self.kwargs['branch']
        college = self.kwargs['college_name']
        semester = self.kwargs['sem']
        books = Book.objects.filter(
            Q(branch__iexact=branch) &
            Q(owner__college__iexact=college) &
            Q(semester=semester)
        )
        return Book.objects.all()


class BookCreateAPIView(generics.GenericAPIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]
    serializer_class = BookCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response('Book created successfully')


class CreatedBooksAPIView(generics.GenericAPIView):
    serializer_class = BookListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        books = self.request.user.books.all()
        return Response({
            'my_books': BookListSerializer(books, many=True).get_unique_for_date_validators
        })


class CollegeList(generics.GenericAPIView):
    serializer_class = CollegeListSerializer
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        college_name = self.kwargs.get('college_name')
        colleges = College.objects.filter(name__icontains=college_name)

        return Response({
            'colleges': CollegeListSerializer(colleges, many=True).data
        })
