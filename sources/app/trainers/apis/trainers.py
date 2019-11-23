from rest_framework import viewsets

from trainers.models import Trainer
from trainers.serializers.trainers import TrainerSerializer


__all___ = (
    'TrainerViewSet',
)


class TrainerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
