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
    descriptions = ExerciseDescriptionSerializer(
        source='exercisedescription_set',
        many=True,
    )
    images = serializers.SerializerMethodField()
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

    def get_images(self, instance):
        trainer = self.context.get('request').query_params.get('trainer')
        return ExerciseImageSerializer(
            instance.exerciseimage_set.filter(trainer=trainer),
            many=True,
        ).data
