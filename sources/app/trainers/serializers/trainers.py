from rest_framework import serializers

from trainers.models import Trainer


class TrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = [
            'pk',
            'name',
            'image_url',
            'impact_image_url',
        ]
