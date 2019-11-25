from django.db import models


__all__ = (
    'BookAuthor',
)


class BookAuthor(models.Model):
    name = models.CharField(
        '저자 명',
        max_length=255,
    )

    def __str__(self):
        return f'책 저자: {self.name}'

    class Meta:
        verbose_name = '저자'
        verbose_name_plural = '저자들'
