from rest_framework import serializers

from accounts.serializers import ContactNumSerializer, UserSerializer

from accounts.models import College
from .models import Book


class BookListSerializer(serializers.ModelSerializer):
    owner = ContactNumSerializer()

    class Meta:
        model = Book
        fields = ['id', 'owner', 'book_name', 'image', 'author', 'cost']


class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['image', 'book_name',
                  'branch', 'semester', 'author', 'cost']



class MyBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','image', 'book_name', 'branch',
                  'semester', 'author', 'cost', 'available']
class CollegeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['id', 'name']
