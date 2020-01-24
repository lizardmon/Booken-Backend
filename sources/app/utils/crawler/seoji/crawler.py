import requests

from utils.errors import ResponseNotExistsError


class SeojiCrawler:
    API_KEY = '0d45bd66aad69ccb535639bcceeb7108'
    URL = 'http://seoji.nl.go.kr/landingPage/SearchApi.do?cert_key={api_key}&result_style=json&page_no=1&page_size=10&isbn={isbn}'

    def __init__(self, isbn):
        self.isbn = isbn

    def do(self):
        url = self.URL.format(
            api_key=self.API_KEY,
            isbn=self.isbn
        )
        response = requests.get(url).json()

        try:
            book_json = response['docs'][0]
        except (KeyError, IndexError):
            raise ResponseNotExistsError

        return {
            'isbn': self.isbn,
            'title': book_json['TITLE'],
            'author': book_json['AUTHOR'],
            'publisher': book_json['PUBLISHER'],
            'page': book_json['PAGE'],
            'sale_prcie': book_json['PRE_PRICE'],
        }
