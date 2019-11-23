from rest_framework import viewsets

from books.models import Book
from books.serializers.books import BookSerializer


__all___ = (
    'BookViewSet',
)


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
