from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from exercises.models import Exercise, ExerciseImage, ExerciseDescription

__all__ = (
    'ExerciseSerializer',
)


class ExerciseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseImage
        fields = [
            'url',
        ]


class ExerciseDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseDescription
        fields = [
            'description',
        ]


class ExerciseSerializer(serializers.ModelSerializer):
    descriptions = ExerciseDescriptionSerializer(
        source='exercisedescription_set',
    )
    images = ExerciseImageSerializer(
        source='exerciseimage_set',
    )

    class Meta:
        model = Exercise
        fields = [
            'id',
            'name',
            'english_name',
            'time',
            'calorie',
            'power',
            'descriptions',
            'images',
        ]


class ExerciseListSerializer(serializers.ModelSerializer):
    from exercises.serializers.exercise_categories import ExerciseCategorySerializer
    descriptions = ExerciseDescriptionSerializer(
        source='exercisedescription_set',
        many=True,
    )
    images = ExerciseImageSerializer(
        source='exerciseimage_set',
        many=True,
    )
    category = ExerciseCategorySerializer()

    class Meta:
        model = Exercise
        fields = [
            'id',
            'name',
            'english_name',
            'time',
            'calorie',
            'power',
            'descriptions',
            'images',
            'category',
        ]
