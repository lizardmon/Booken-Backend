from rest_framework import serializers

from exercises.models import Exercise, ExerciseImage

__all__ = ("ExerciseSerializer", "ExerciseListSerializer")


class ExerciseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseImage
        fields = ["url"]


class ExerciseSerializer(serializers.ModelSerializer):
    descriptions = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='description',
        source="exercisedescription_set",
    )
    images = ExerciseImageSerializer(source="exerciseimage_set", many=True)

    class Meta:
        model = Exercise
        fields = [
            "id",
            "name",
            "english_name",
            "time",
            "calorie",
            "power",
            "descriptions",
            "images",
        ]


class ExerciseListSerializer(serializers.ModelSerializer):
    from exercises.serializers.exercise_categories import (  # pylint: disable=C0415,R0401
        ExerciseCategorySerializer,
    )

    descriptions = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='description',
        source="exercisedescription_set",
    )
    images = ExerciseImageSerializer(source="exerciseimage_set", many=True)
    category = ExerciseCategorySerializer()

    class Meta:
        model = Exercise
        fields = [
            "id",
            "name",
            "english_name",
            "time",
            "calorie",
            "power",
            "descriptions",
            "images",
            "category",
        ]
