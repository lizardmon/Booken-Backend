from rest_framework.exceptions import APIException


class ISBNNotExistsError(APIException):
    status_code = 400
    default_detail = '해당 ISBN이 존재하지 않습니다.'
    default_code = 'isbn_does_not_exists'


class ResponseNotExistsError(Exception):
    def __str__(self):
        return '해당 정보가 존재하지 않습니다.'
