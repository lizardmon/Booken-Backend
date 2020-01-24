import asyncio

from django.db import models, transaction

from books.models import BookAuthor, BookPublisher  # pylint: disable=R0401
from utils.crawler.seoji.crawler import SeojiCrawler
from utils.crawler.yes24.crawler import Yes24Crawler
from utils.django.models import get_remote_image
from utils.errors import ResponseNotExistsError

__all__ = ("Book",)


def image_file_name(instance, filename):
    return "/".join(["books", instance.name, filename])


class Book(models.Model):
    isbn = models.CharField("ISBN", max_length=255)
    name = models.CharField("이름", max_length=255)
    weight = models.IntegerField("무게", null=True)
    page = models.IntegerField("페이지", null=True)
    sale_price = models.IntegerField("판매 가격", null=True)
    used_price = models.IntegerField("중고 가격", null=True)
    grade = models.FloatField("평점", null=True)
    cover_image_url = models.ImageField("커버 이미지", null=True, upload_to=image_file_name)

    author = models.ForeignKey(BookAuthor, verbose_name="저자", on_delete=models.CASCADE)
    publisher = models.ForeignKey(
        BookPublisher, verbose_name="출판사", on_delete=models.CASCADE
    )

    # TODO: Reviews 모델 생성 해야함

    def __str__(self):
        return f"책: {self.name}, 평정: {self.grade}"

    class Meta:
        verbose_name = "책"
        verbose_name_plural = "책들"

    def isbn_create(self, isbn):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            yes24_response = loop.run_until_complete(
                Yes24Crawler(isbn).do()
            )
        except ResponseNotExistsError:
            raise ResponseNotExistsError()
        finally:
            loop.close()

        self.isbn = isbn
        self.name = yes24_response.get("name")
        self.weight = yes24_response.get('weight')
        self.page = yes24_response.get('page')
        self.sale_price = yes24_response.get('sale_price')
        # 중고가
        self.grade = yes24_response.get('rating')

        with transaction.atomic():
            author, _ = BookAuthor.objects.get_or_create(name=yes24_response.get('author'))
            publisher, _ = BookPublisher.objects.get_or_create(
                name=yes24_response.get("publisher")
            )

            self.author = author
            self.publisher = publisher

            self.cover_image_url.save(self.name + '.jpg', get_remote_image(yes24_response.get('image_url')))
            self.save()

        return self
