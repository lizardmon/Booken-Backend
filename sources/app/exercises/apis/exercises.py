from django.db.models import Prefetch
from django.utils.decorators import method_decorator

from drf_yasg.utils import swagger_auto_schema
from exercises.models import Exercise, ExerciseImage
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

    def get_queryset(self):
        queryset = super().get_queryset()
        trainer_id = self.request.query_params.get('trainer', None)
        if trainer_id is not None:
            queryset = queryset.prefetch_related(
                Prefetch(
                    'exerciseimage_set',
                    queryset=ExerciseImage.objects.filter(trainer=trainer_id)
                )
            )
        return queryset
