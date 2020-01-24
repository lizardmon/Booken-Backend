from bs4 import BeautifulSoup
from pyppeteer import launch

from utils.errors import ResponseNotExistsError


class Yes24Crawler:
    BASE_URL = 'http://www.yes24.com/searchcorner/Search?'
    QUERY = 'query={isbn}'

    def __init__(self, isbn):
        self.isbn = isbn

        self.browser = None
        self.page = None

    async def do(self):
        self.browser = await launch(
            {'args': ['--no-sandbox', '--disable-setuid-sandbox']},
            handleSIGINT=False,
            handleSIGTERM=False,
            handleSIGHUP=False,
        )
        self.page = await self.browser.newPage()

        await self.search_book_by_isbn()
        await self.goto_book_detail_page()
        book_info = await self.parse_book_info()

        await self.browser.close()

        return book_info

    async def search_book_by_isbn(self):
        """
        ISBN 으로 책 검색
        """
        response = await self.page.goto(
            self.BASE_URL + self.QUERY.format(isbn=self.isbn)
        )

        if await self.page.J('.area_no_result'):
            raise ResponseNotExistsError()

        await self.page.waitForSelector('.goods_list_wrap .goodsList.goodsList_list')

    async def goto_book_detail_page(self):
        """
        검색된 책의 상세페이지로 이동
        """
        a_element = await self.page.J('.goods_name.goods_icon > a')
        await a_element.click()

    def parse_review(self, review):
        review_rating_target = '.cmtInfoBox > .cmt_rating > span.rating'
        review_content_target = '.cmtInfoBox > .cmt_cont > span.txt'
        review_nickname_target = '.cmt_etc > .txt_id > a.lnk_nick'
        review_created_at_target = '.cmt_etc > .txt_date'

        rating = review.select_one(review_rating_target).get_text()
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

    async def get_reviews(self):
        # 리뷰 목록이 로딩되었는지 확인
        review_load_target = '#infoset_oneCommentList > .rvCmt_sort'

        # review_page_list 는 활성화된(현재 페이지)의 숫자는 제외하고 가져온다.
        review_page_list_target = review_load_target + ':nth-of-type(2) > .rvCmt_sortLft > .yesUI_pagenS > a.num'
        review_next_page_target = review_load_target + ':nth-of-type(2) > .rvCmt_sortLft > .yesUI_pagenS > a.bgYUI.next'

        # 리뷰 컨텐츠 Target
        review_content_load_target = '#infoset_oneCommentList > .infoSetCont_wrap'
        review_content_group_target = review_content_load_target + ' > .cmtInfoGrp'

        result = []

        while True:
            # review_page_list 를 모두 돌고
            # last_page 가 dim 클래스를 가지고 있으면 종료

            # 리뷰 로딩 대기
            await self.page.waitForSelector(review_content_load_target)

            # 첫 페이지는 그냥 가져와야함
            html = await self.page.content()
            soup = BeautifulSoup(html, 'html.parser')
            reviews = soup.select(review_content_group_target)
            result += self.parse_reviews(reviews)

            review_page_list = soup.select(review_page_list_target)

            for index, one_page in enumerate(review_page_list):
                target_review_page_list = await self.page.JJ(review_page_list_target)
                await target_review_page_list[index].click()
                await self.page.waitForSelector(review_content_load_target)

                html = await self.page.content()
                soup = BeautifulSoup(html, 'html.parser')
                reviews = soup.select(review_content_group_target)
                result += self.parse_reviews(reviews)

            # 다음 페이지가 없으면 dim 속성이 존재한다.
            html = await self.page.content()
            soup = BeautifulSoup(html, 'html.parser')
            if soup.select_one(review_next_page_target + '.dim'):
                print('done')
                break
            else:
                next_page_target = await self.page.J(review_next_page_target)
                await next_page_target.click()
                await self.page.waitFor(200)

        return result

    async def parse_book_info(self):
        name_target = '#yDetailTopWrap > .topColRgt > .gd_infoTop h2.gd_name'
        author_target = '#yDetailTopWrap > .topColRgt > .gd_infoTop .gd_pubArea > .gd_auth > a'
        publisher_target = '#yDetailTopWrap > .topColRgt > .gd_infoTop .gd_pubArea > .gd_pub > a'
        sale_price_target = '#yDetailTopWrap > .topColRgt > .gd_infoBot .nor_price > em.yes_m'
        image_target = '#yDetailTopWrap .imgBdr > img'
        rating_target = '#yDetailTopWrap > .topColRgt > .gd_infoTop #spanGdRating em.yes_b'
        page_weight_size_target = '#infoset_specific tr:nth-of-type(2) .lastCol'

        await self.page.waitForSelector(page_weight_size_target)
        html = await self.page.content()
        soup = BeautifulSoup(html, 'html.parser')

        name = soup.select_one(name_target).get_text()
        sale_price = ''.join(
            filter(
                str.isdigit,
                soup.select_one(sale_price_target).get_text()
            )
        ) if soup.select_one(sale_price_target) else None
        author = soup.select_one(author_target).get_text()
        publisher = soup.select_one(publisher_target).get_text()
        image_url = soup.select_one(image_target).get('src') if soup.select_one(image_target) else None
        rating = soup.select_one(rating_target).get_text() if soup.select_one(rating_target) else None
        page_weight_size = soup.select_one(page_weight_size_target).get_text().split('|')

        page, weight, size = None, None, None

        for item in page_weight_size:
            if '쪽' in item:
                page = ''.join(filter(str.isdigit, item))
            elif 'g' in item:
                weight = ''.join(filter(str.isdigit, item))
            elif 'mm' in item:
                size = item.strip()

        return {
            'name': name,
            'sale_price': sale_price,
            'author': author,
            'publisher': publisher,
            'image_url': image_url,
            'rating': rating,
            'page': page,
            'weight': weight,
            'size': size,
        }
