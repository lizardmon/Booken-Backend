# Generated by Django 2.2.7 on 2019-11-23 16:20

import books.models.books
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='저자 명')),
            ],
            options={
                'verbose_name': '저자',
                'verbose_name_plural': '저자들',
            },
        ),
        migrations.CreateModel(
            name='BookPublisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='출판사 명')),
            ],
            options={
                'verbose_name': '출판사',
                'verbose_name_plural': '출판사들',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=255, verbose_name='ISBN')),
                ('name', models.CharField(max_length=255, verbose_name='이름')),
                ('weight', models.IntegerField(null=True, verbose_name='무게')),
                ('page', models.IntegerField(null=True, verbose_name='페이지')),
                ('sale_price', models.IntegerField(null=True, verbose_name='판매 가격')),
                ('used_price', models.IntegerField(null=True, verbose_name='중고 가격')),
                ('grade', models.FloatField(null=True, verbose_name='평점')),
                ('cover_image_url', models.ImageField(null=True, upload_to=books.models.books.image_file_name, verbose_name='커버 이미지')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.BookAuthor', verbose_name='저자')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.BookPublisher', verbose_name='출판사')),
            ],
            options={
                'verbose_name': '책',
                'verbose_name_plural': '책들',
            },
        ),
    ]
