from django.utils.decorators import method_decorator

from drf_yasg.utils import swagger_auto_schema
from exercises.models import Exercise
from exercises.serializers.exercises import ExerciseListSerializer
from rest_framework import viewsets

__all___ = ("ExerciseViewSet",)


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Exercise List", operation_description="운동 목록"
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_summary="Get Exercise", operation_description="운동 하나"
    ),
)
class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    운동 API
    """

    queryset = Exercise.objects.all()
    serializer_class = ExerciseListSerializer
