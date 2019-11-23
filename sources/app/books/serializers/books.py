from rest_framework import serializers

from books.models import Book
from books.serializers.book_publishers import BookPublisherSerializer
from books.serializers.books_authors import BookAuthorSerializer


class BookSerializer(serializers.ModelSerializer):
    author = BookAuthorSerializer()
    publisher = BookPublisherSerializer()

    class Meta:
        model = Book
        fields = [
            'id',
            'name',
            'isbn',
            'weight',
            'page',
            'sale_price',
            'used_price',
            'grade',
            'cover_image_url',
            'author',
            'publisher',
        ]
