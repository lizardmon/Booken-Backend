from urllib import request

from django.core.files import File


def get_remote_image(image_url):
    result = request.urlretrieve(image_url)
    return File(open(result[0], 'rb'))
