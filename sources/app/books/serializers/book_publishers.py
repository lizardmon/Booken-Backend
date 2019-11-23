from rest_framework import serializers

from books.models import BookPublisher


class BookPublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookPublisher
        fields = [
            'pk',
            'name',
        ]
