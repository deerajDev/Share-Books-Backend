from rest_framework.pagination import PageNumberPagination


class BookListPaginator(PageNumberPagination):
    page_size= 10