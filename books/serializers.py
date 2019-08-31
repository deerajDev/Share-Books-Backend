from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Book


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'owner', 'book_name', 'image', 'author', 'cost']
        depth = 1


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'image', 'book_name',
                  'branch', 'semester', 'author', 'cost']
