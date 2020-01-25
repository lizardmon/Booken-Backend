from rest_framework import serializers

from books.models import BookReview


class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = [
            'id',
            'rating',
            'content',
            'nickname',
            'created_at',
        ]
