import asyncio

from celery import shared_task
from celery.utils.log import get_task_logger
from django.db import models

from books.models import Book
from config.celery_app import app
from utils.crawler.yes24.crawler import Yes24Crawler
from utils.errors import ResponseNotExistsError


__all__ = ("BookReview",)


class BookReview(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name='책',
    )
    rating = models.IntegerField('평점')
    content = models.TextField('한줄평')
    nickname = models.CharField('닉네임', max_length=20)
    created_at = models.DateField('리뷰일')

    def __str__(self):
        return f'{self.nickname}: {self.content}'

    class Meta:
        verbose_name = '리뷰'
        verbose_name_plural = '리뷰들'

    @staticmethod
    @app.task
    def get_reviews(book_id):
        book = Book.objects.get(id=book_id)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            yes24_response = loop.run_until_complete(
                Yes24Crawler(book.isbn).do_reviews()
            )
        except ResponseNotExistsError:
            raise ResponseNotExistsError()
        finally:
            loop.close()

        bulk_review_list = []

        for review in yes24_response:
            bulk_review_list.append(
                BookReview(
                    book=book,
                    **review
                )
            )

        result = BookReview.objects.bulk_create(bulk_review_list)

        return len(result)
