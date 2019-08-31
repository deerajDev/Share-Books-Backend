from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['author','book_name','branch','semester']
    search_fields = ['author','book_name']
    filter_fields = ['book_name','author','branch','semester','cost']
