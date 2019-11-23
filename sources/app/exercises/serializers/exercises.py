from rest_framework import serializers

from exercises.models import Exercise, ExerciseImage


class ExerciseImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseImage
        fields = [
            'pk',
            'url',
            'ordering',
        ]


class ExerciseSerializer(serializers.ModelSerializer):
    images = ExerciseImagesSerializer(many=True)

    class Meta:
        model = Exercise
        fields = [
            'pk',
            'name',
            'description',
            'calorie',
            'power',
            'images',
        ]
