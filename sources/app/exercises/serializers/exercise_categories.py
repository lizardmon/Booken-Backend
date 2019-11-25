from exercises.models import ExerciseCategory
from rest_framework import serializers

__all__ = ("ExerciseCategorySerializer", "ExerciseCategoryListSerializer")


class ExerciseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseCategory
        fields = ["id", "name", "description"]


class ExerciseCategoryListSerializer(serializers.ModelSerializer):
    from exercises.serializers.exercises import (  # pylint: disable=C0415,R0401
        ExerciseSerializer,
    )

    exercises = ExerciseSerializer(source="exercise_set", many=True)

    class Meta:
        model = ExerciseCategory
        fields = ["id", "name", "description", "exercises"]
