from django.db import models

__all__ = ("ExerciseCategory",)


class ExerciseCategory(models.Model):
    name = models.CharField("이름", max_length=255)
    description = models.TextField("설명", blank=True)

    def __str__(self):
        return f"운동 카테고리: {self.name}"

    class Meta:
        verbose_name = "운동 카테고리"
        verbose_name_plural = "운동 카테고리들"
