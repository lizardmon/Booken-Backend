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
    descriptions = serializers.ListField(
        source='description_set',
    )
    images = ExerciseImagesSerializer(many=True)

    class Meta:
        model = Exercise
        fields = [
            'pk',
            'name',
            'calorie',
            'power',
            'descriptions',
            'images',
        ]
