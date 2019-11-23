from django.db import models


def image_file_name(instance, filename):
    return '/'.join(['trainers', instance.name, filename])


class Trainer(models.Model):
    name = models.CharField(
        '이름',
        max_length=255,
    )
    image_url = models.ImageField(
        '트레이너 이미지',
        upload_to=image_file_name,
    )
    impact_image_url = models.ImageField(
        '트레이너 선택 이미지',
        upload_to=image_file_name,
    )

    def __str__(self):
        return f'트레이너 {self.name} 님'

    class Meta:
        verbose_name = '트레이너'
        verbose_name_plural = '트레이너들'
