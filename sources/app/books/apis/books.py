from django.http import Http404
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from books.models import Book
from books.serializers.books import BookSerializer
from utils.errors import ISBNNotExistsError, ResponseNotExistsError

__all___ = ("BookViewSet",)


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Book List", operation_description="책 목록"
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_summary="Get Book", operation_description="책 하나"
    ),
)
class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """
    책 API
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "isbn"

    def get_object(self):
        try:
            instance = super().get_object()
        except Http404:
            try:
                instance = Book().isbn_create(self.kwargs.get('isbn'))
            except ResponseNotExistsError:
                raise ISBNNotExistsError

        return instance
