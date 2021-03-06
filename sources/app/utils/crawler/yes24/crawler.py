import requests
from bs4 import BeautifulSoup


from utils.errors import ResponseNotExistsError


class Yes24Crawler:
    BASE_URL = 'http://www.yes24.com'
    SEARCH_URL = '/searchcorner/Search?'
    DETAIL_URL = '/Product/Goods/{yes24_book_id}'
    REVIEW_URL = '/Product/communityModules/AwordReviewList/{yes24_book_id}?PageNumber={page_number}'

    def __init__(self, isbn=None, yes24_book_id=None):
        self.isbn = isbn
        self.yes24_book_id = yes24_book_id

        self.page = None

    def get_yes24_book_id(self):
        if not self.yes24_book_id:
            self._get_yes24_book_id()
        return self.yes24_book_id

    def do_reviews(self):
        self.get_yes24_book_id()
        reviews = self.get_reviews()

        return reviews

    def do(self):
        self.get_yes24_book_id()
        book_info = self.parse_book_info()

        return book_info

    def _get_yes24_book_id(self):
        """
        검색된 책의 ID 를 가져옴
        """
        href_target = '.goods_name.goods_icon > a'
        no_result = '.area_no_result'

        html = requests.get(
            self.BASE_URL + self.SEARCH_URL + f'query={self.isbn}'
        ).content
        soup = BeautifulSoup(html, 'html.parser')

        if soup.select(no_result):
            raise ResponseNotExistsError()

        href = soup.select_one(href_target).get('href')
        self.yes24_book_id = href.split('/Product/Goods/')[1].split('?')[0]

        return self.yes24_book_id

    def parse_review(self, review):
        review_rating_target = '.cmtInfoBox > .cmt_rating > span.rating'
        review_content_target = '.cmtInfoBox > .cmt_cont > span.txt'
        review_nickname_target = '.cmt_etc > .txt_id > a.lnk_nick'
        review_created_at_target = '.cmt_etc > .txt_date'

        rating = float(
            ''.join(
                filter(
                    str.isdigit,
                    review.select_one(review_rating_target).get_text()
                )
            )
        ) if review.select_one(review_rating_target) else None
        content = review.select_one(review_content_target).get_text()
        nickname = review.select_one(review_nickname_target).get_text()
        created_at = review.select_one(review_created_at_target).get_text()

        return {
            'rating': rating,
            'content': content,
            'nickname': nickname,
            'created_at': created_at,
        }

    def parse_reviews(self, reviews):
        results = []

        for review in reviews:
            results.append(
                self.parse_review(review)
            )

        return results

    def get_reviews(self):
        # 한줄 평 없는 지 확인
        review_no_comment_target = '.noData'

        # 리뷰 컨텐츠 Target
        review_content_group_target = '.infoSetCont_wrap > .cmtInfoGrp'

        page_number = 1
        result = []

        while True:
            html = requests.get(
                self.BASE_URL + self.REVIEW_URL.format(
                    yes24_book_id=self.yes24_book_id,
                    page_number=page_number,
                )
            ).content
            page_number += 1
            soup = BeautifulSoup(html, 'html.parser')
            reviews_soup = soup.select(review_content_group_target)

            # 최대 30 페이지까지만
            if soup.select_one(review_no_comment_target) or page_number == 30:
                break

            result += self.parse_reviews(reviews_soup)

        return result

    def parse_book_info(self):
        name_target = '#yDetailTopWrap > .topColRgt > .gd_infoTop h2.gd_name'
        isbn_target = '#infoset_specific tr:nth-of-type(3) .lastCol'
        author_target = '#yDetailTopWrap > .topColRgt > .gd_infoTop .gd_pubArea > .gd_auth'
        publisher_target = '#yDetailTopWrap > .topColRgt > .gd_infoTop .gd_pubArea > .gd_pub'
        sale_price_target = '#yDetailTopWrap > .topColRgt > .gd_infoBot .nor_price > em.yes_m'
        image_target = '#yDetailTopWrap .imgBdr > img'
        rating_target = '#yDetailTopWrap > .topColRgt > .gd_infoTop #spanGdRating em.yes_b'
        page_weight_size_target = '#infoset_specific tr:nth-of-type(2) .lastCol'

        html = requests.get(self.BASE_URL + self.DETAIL_URL.format(yes24_book_id=self.yes24_book_id)).content
        soup = BeautifulSoup(html, 'html.parser')

        name = soup.select_one(name_target).get_text()
        isbn = soup.select_one(isbn_target).get_text()
        sale_price = ''.join(
            filter(
                str.isdigit,
                soup.select_one(sale_price_target).get_text()
            )
        ) if soup.select_one(sale_price_target) else None
        author = soup.select_one(author_target).get_text(strip=True)
        publisher = soup.select_one(publisher_target).get_text(strip=True)
        image_url = soup.select_one(image_target).get('src') if soup.select_one(image_target) else None
        rating = soup.select_one(rating_target).get_text() if soup.select_one(rating_target) else None
        page_weight_size = soup.select_one(page_weight_size_target).get_text().split('|')

        page, weight, size = None, None, None

        for item in page_weight_size:
            if '쪽' in item:
                page = ''.join(filter(str.isdigit, item))
                # 쪽수 확인 중인게 있음
                page = page if page else None
            elif 'g' in item:
                weight = ''.join(filter(str.isdigit, item))
            elif 'mm' in item:
                size = item.strip()

        return {
            'yes24_book_id': self.yes24_book_id,
            'name': name,
            'isbn': isbn,
            'sale_price': sale_price,
            'author': author,
            'publisher': publisher,
            'image_url': image_url,
            'rating': rating,
            'page': page,
            'weight': weight,
            'size': size,
        }
