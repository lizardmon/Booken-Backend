# Generated by Django 2.2.8 on 2020-01-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_yes24_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=255, unique=True, verbose_name='ISBN'),
        ),
    ]
