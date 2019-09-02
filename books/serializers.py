from rest_framework import serializers

from accounts.serializers import UserSerializer

from .models import Book


class BookListSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Book
        fields = ['id', 'owner', 'book_name', 'image', 'author', 'cost']


class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['image', 'book_name',
                  'branch', 'semester', 'author', 'cost']
