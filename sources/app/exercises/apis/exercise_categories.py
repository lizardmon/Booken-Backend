from django.utils.decorators import method_decorator

from drf_yasg.utils import swagger_auto_schema
from exercises.models import ExerciseCategory
from exercises.serializers.exercise_categories import ExerciseCategoryListSerializer
from rest_framework import viewsets

__all___ = ("ExerciseCategoryViewSet",)


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Exercise Category List",
        operation_description="운동 목록 (카테고리 그룹핑)",
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_summary="Get Exercise Category",
        operation_description="운동 하나 (카테고리 그룹핑)",
    ),
)
class ExerciseCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    운동 카테고리 API
    """

    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategoryListSerializer
