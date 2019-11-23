from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from books.models import Book
from books.serializers.books import BookSerializer


__all___ = (
    'BookViewSet',
)

@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        operation_summary='Book List',
        operation_description='책 목록',
    )
)
@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_summary='Get Book',
        operation_description='책 하나',
    )
)
class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """
    책 API
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = [
        'isbn',
    ]
