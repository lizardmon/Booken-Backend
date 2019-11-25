from django.utils.decorators import method_decorator

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from trainers.models import Trainer
from trainers.serializers.trainers import TrainerSerializer

__all___ = ("TrainerViewSet",)


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Trainer List", operation_description="트레이너 목록"
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_summary="Get Trainer", operation_description="트레이너 한명"
    ),
)
class TrainerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    트레이너 API
    """

    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
