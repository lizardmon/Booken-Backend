from django.db import models

__all__ = (
    'BookPublisher',
)


class BookPublisher(models.Model):
    name = models.CharField(
        '출판사 명',
        max_length=255,
    )

    def __str__(self):
        return f'출판사: {self.name}'

    class Meta:
        verbose_name = '출판사'
        verbose_name_plural = '출판사들'
