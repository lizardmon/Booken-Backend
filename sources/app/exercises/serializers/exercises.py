from rest_framework import serializers

from exercises.models import Exercise, ExerciseImage

__all__ = (
    'ExerciseSerializer',
)


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
    images = serializers.ListField(
        source='image_set',
    )

    class Meta:
        model = Exercise
        fields = [
            'pk',
            'name',
            'time',
            'calorie',
            'power',
            'descriptions',
            'images',
        ]


class ExerciseListSerializer(serializers.ModelSerializer):
    from exercises.serializers.exercise_categories import ExerciseCategorySerializer
    descriptions = serializers.ListField(
        source='description_set',
    )
    images = serializers.ListField(
        source='image_set',
    )
    category = ExerciseCategorySerializer()

    class Meta:
        model = Exercise
        fields = [
            'pk',
            'name',
            'time',
            'calorie',
            'power',
            'descriptions',
            'images',
            'category',
        ]
