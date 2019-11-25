from books.models import BookAuthor
from rest_framework import serializers


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = [
            'id',
            'name',
        ]
