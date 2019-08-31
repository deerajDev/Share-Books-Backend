from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Book
from .serializers import BookListSerializer, BookCreateSerializer


class BookListAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookListSerializer

    def post(self, request, *args, **kwargs):
        print('='*20)
        serializer = self.get_serializer(data=request.data)
        print(vars(serializer))
        print('='*20)
        return Response('it is from post data')


class BookCreateAPIView(generics.GenericAPIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]
    serializer_class = BookCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response('Book created successfully')
