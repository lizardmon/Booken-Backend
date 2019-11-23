from rest_framework import serializers

from exercises.models import ExerciseCategory
from exercises.serializers.exercises import ExerciseSerializer


class ExerciseCategorySerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = ExerciseCategory
        fields = [
            'pk',
            'name',
            'description',
            'exercises',
        ]
