from rest_framework.pagination import PageNumberPagination


class BookListPaginator(PageNumberPagination):
    page_size = 5


class MyBooksPaginator(PageNumberPagination):
    page_size = 1
