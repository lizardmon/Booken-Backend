from django.db import models

from trainers.models import Trainer
from .exercise_category import ExerciseCategory

__all__ = (
    'Exercise',
    'ExerciseImage',
)


def image_file_name(instance, filename):
    return '/'.join(['trainers', instance.trainer.name, 'exercise', filename])


class Exercise(models.Model):
    EXERCISE_CHOICES = (
        ('weak', '약함'),
        ('normal', '보통'),
        ('strong', '강함'),
    )

    name = models.CharField(
        '이름',
        max_length=255,
    )
    english_name = models.CharField(
        '영어 이름',
        max_length=255,
    )
    calorie = models.IntegerField(
        '칼로리',
        blank=True,
        null=True,
    )
    time = models.IntegerField(
        '시간',
        blank=True,
        null=True,
    )

    power = models.CharField(
        max_length=255,
        choices=EXERCISE_CHOICES,
        blank=True,
        null=True,
    )

    category = models.ForeignKey(
        ExerciseCategory,
        verbose_name='카테고리',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'운동: {self.name}, 칼로리: {self.calorie}'

    class Meta:
        verbose_name = '운동'
        verbose_name_plural = '운동들'


class ExerciseImage(models.Model):
    ordering = models.IntegerField(
        verbose_name='순서',
    )
    url = models.ImageField(
        verbose_name='이미지',
        upload_to=image_file_name,
    )
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
    )

    exercise = models.ForeignKey(
        Exercise,
        verbose_name='운동',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'운동 이미지 {self.ordering}'

    class Meta:
        verbose_name = '운동 이미지'
        verbose_name_plural = '운동 이미지들'
        ordering = ['ordering']
