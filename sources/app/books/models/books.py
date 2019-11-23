from django.db import models

from books.models import BookAuthor, BookPublisher


def image_file_name(instance, filename):
    return '/'.join(['books', instance.name, filename])


class Book(models.Model):
    isbn = models.CharField(
        'ISBN',
        max_length=255,
    )
    name = models.CharField(
        '이름',
        max_length=255,
    )
    weight = models.IntegerField(
        '무게',
    )
    page = models.IntegerField(
        '페이지',
    )
    sale_price = models.IntegerField(
        '판매 가격',
    )
    used_price = models.IntegerField(
        '중고 가격',
    )
    grade = models.FloatField(
        '평점',
    )
    cover_image_url = models.ImageField(
        '커버 이미지',
        upload_to=image_file_name,
    )

    author = models.ForeignKey(
        BookAuthor,
        verbose_name='저자',
        on_delete=models.CASCADE,
    )
    publisher = models.ForeignKey(
        BookPublisher,
        verbose_name='출판사',
        on_delete=models.CASCADE,
    )
    # TODO: Reviews 모델 생성 해야함

    def __str__(self):
        return f'책: {self.name}, 평정: {self.grade}'

    class Meta:
        verbose_name = '책'
        verbose_name_plural = '책들'
