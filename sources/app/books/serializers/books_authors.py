from rest_framework import serializers

from books.models import BookAuthor


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = [
            'id',
            'name',
        ]
