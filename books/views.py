from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import serializers
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from accounts.models import College
from .models import Book
from .serializers import BookCreateSerializer, BookListSerializer,MyBooksSerializer , CollegeListSerializer
from .pagination import BookListPaginator, MyBooksPaginator

from .helpers import updateBook
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
            Q(semester=semester) &
            Q(available=True)
        )
        return books


class BookCreateAPIView(generics.GenericAPIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]
    serializer_class = BookCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_book = serializer.save(owner=request.user)
        return Response(f'{request.user}')


class CreatedBooksAPIView(generics.GenericAPIView):
    serializer_class = BookListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        books = self.request.user.books.all()
        return Response({
            'my_books': BookListSerializer(books, many=True).get_unique_for_date_validators
        })


class MyBooksAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MyBooksSerializer
    pagination_class = MyBooksPaginator
    def get_queryset(self, *args, **kwargs):
        my_books = self.request.user.books.all()
        return my_books
    

class UpdateBookAPIView(generics.GenericAPIView):
    serializer_class = BookCreateSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        new_data = request.data
        instance = get_object_or_404(Book, pk=id)
        updateBook(instance, new_data)
        return Response('it was succesful')
        # if not (instance.owner == request.user):
        #     raise serializers.ValidationError('Your are not the owner of this book')
        # else:
        #     try:
        #         updateBook(instance, new_data)
        #         return Response('Update successful')
        #     except Exception as e:
        #         raise serializers.ValidationError('Update failed')


class CollegeList(generics.GenericAPIView):
    serializer_class = CollegeListSerializer
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        college_name = self.kwargs.get('college_name')
        colleges = College.objects.filter(name__icontains=college_name)

        return Response({
            'colleges': CollegeListSerializer(colleges, many=True).data
        })

