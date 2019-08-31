from django.urls import path
from .views import BookListAPIView, BookCreateAPIView

app_name = 'books'

urlpatterns = [
    path("list", BookListAPIView.as_view(), name="list"),
    path("create", BookCreateAPIView.as_view(), name="create"),
]
