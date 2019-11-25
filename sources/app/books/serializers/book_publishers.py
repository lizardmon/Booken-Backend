from books.models import BookPublisher
from rest_framework import serializers


class BookPublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookPublisher
        fields = [
            'id',
            'name',
        ]
