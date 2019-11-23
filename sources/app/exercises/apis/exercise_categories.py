from rest_framework import viewsets

from exercises.models import ExerciseCategory
from exercises.serializers.exercise_categories import ExerciseCategorySerializer


__all___ = (
    'ExerciseCategoryViewSet',
)


class ExerciseCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategorySerializer
