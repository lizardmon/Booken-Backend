from django.db import models, transaction

import requests
from books.models import BookAuthor, BookPublisher  # pylint: disable=R0401
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
        api_key = "0d45bd66aad69ccb535639bcceeb7108"
        url = (
            f"http://seoji.nl.go.kr/landingPage/SearchApi.do?"
            f"cert_key={api_key}&result_style=json&page_no=1&page_size=10&isbn={isbn}"
        )

        response = requests.get(url).json()

        try:
            book_json = response["docs"][0]
        except (KeyError, IndexError):
            # 400 Error
            raise ResponseNotExistsError

        self.isbn = isbn
        self.name = book_json["TITLE"]
        # 무게
        page = "".join(x for x in book_json["PAGE"] if x.isdigit())
        self.page = page if page else None
        self.sale_price = book_json["PRE_PRICE"]
        # 중고가
        # 평점
        # 커버 이미지

        with transaction.atomic():
            author, _ = BookAuthor.objects.get_or_create(name=book_json["AUTHOR"])
            publisher, _ = BookPublisher.objects.get_or_create(
                name=book_json["PUBLISHER"]
            )

            self.author = author
            self.publisher = publisher
            self.save()

        return self
