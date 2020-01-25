from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from books.models import Book
from books.serializers.book_reviews import BookReviewSerializer

__all___ = ("BookReviewListAPIView",)


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Book Review List", operation_description="책 리뷰 목록"
    ),
)
class BookReviewListAPIView(generics.ListAPIView):
    """
    책 리뷰 API
    """
    queryset = Book.objects.all()
    serializer_class = BookReviewSerializer

    def get_queryset(self):
        book = get_object_or_404(Book, isbn=self.kwargs.get('isbn'))
        return book.bookreview_set.all()
