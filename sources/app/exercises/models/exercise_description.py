from django.db import models

from exercises.models import Exercise

__all__ = ("ExerciseDescription",)


class ExerciseDescription(models.Model):
    description = models.TextField("운동 설명")
    ordering = models.IntegerField("운동 정렬")

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return f"운동설명 {self.description}"

    class Meta:
        ordering = ["ordering"]
        verbose_name = "운동 설명"
        verbose_name_plural = "운동 설명들"
