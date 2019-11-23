from rest_framework import viewsets

from exercises.models import Exercise
from exercises.serializers.exercises import ExerciseSerializer


__all___ = (
    'ExerciseViewSet',
)


class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
