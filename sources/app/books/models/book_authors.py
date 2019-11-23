from django.db import models


class BookAuthor(models.Model):
    name = models.CharField(
        '저자 명',
        max_length=255,
    )

    class Meta:
        verbose_name = '저자'
        verbose_name_plural = '저자들'
