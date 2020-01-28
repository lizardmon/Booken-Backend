import asyncio

from django.apps import apps
from django.db import models, transaction, IntegrityError
from django.db.transaction import on_commit

from utils.crawler.yes24.crawler import Yes24Crawler
from utils.django.models import get_remote_image
from utils.errors import ResponseNotExistsError

__all__ = ("Book",)


def image_file_name(instance, filename):
    return "/".join(["books", instance.name, filename])


class Book(models.Model):
    isbn = models.CharField("ISBN", max_length=255, unique=True,)
    name = models.CharField("이름", max_length=255)
    weight = models.IntegerField("무게", null=True)
    page = models.IntegerField("페이지", null=True)
    sale_price = models.IntegerField("판매 가격", null=True)
    used_price = models.IntegerField("중고 가격", null=True)
    grade = models.FloatField("평점", null=True)
    cover_image_url = models.ImageField("커버 이미지", null=True, upload_to=image_file_name)

    yes24_book_id = models.IntegerField('Yes24 책 ID', null=True)

    author = models.ForeignKey('BookAuthor', verbose_name="저자", on_delete=models.CASCADE)
    publisher = models.ForeignKey(
        'BookPublisher', verbose_name="출판사", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"책: {self.name}, 평정: {self.grade}"

    class Meta:
        verbose_name = "책"
        verbose_name_plural = "책들"

    def isbn_create(self, isbn):

        try:
            yes24_response = Yes24Crawler(isbn).do()
        except ResponseNotExistsError:
            raise ResponseNotExistsError()

        self.yes24_book_id = yes24_response.get('yes24_book_id')
        self.isbn = yes24_response.get('isbn')
        self.name = yes24_response.get('name')
        self.weight = yes24_response.get('weight')
        self.page = yes24_response.get('page')
        self.sale_price = yes24_response.get('sale_price')
        # 중고가
        self.grade = yes24_response.get('rating')

        BookAuthor = apps.get_model(app_label='books', model_name='BookAuthor')
        BookPublisher = apps.get_model(app_label='books', model_name='BookPublisher')
        BookReview = apps.get_model(app_label='books', model_name='BookReview')

        try:
            with transaction.atomic():
                author, _ = BookAuthor.objects.get_or_create(name=yes24_response.get('author'))
                publisher, _ = BookPublisher.objects.get_or_create(
                    name=yes24_response.get('publisher')
                )

                self.author = author
                self.publisher = publisher

                self.cover_image_url.save(self.name + '.jpg', get_remote_image(yes24_response.get('image_url')))
                self.save()
        except IntegrityError:
            # 중복 ISBN 이 있을 경우 해당 Object Return
            return self.objects.get(isbn=isbn)

        on_commit(lambda: BookReview.get_reviews.delay(self.id))

        return self
