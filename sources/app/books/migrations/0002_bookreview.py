# Generated by Django 2.2.8 on 2020-01-25 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(verbose_name='평점')),
                ('content', models.TextField(verbose_name='한줄평')),
                ('nickname', models.CharField(max_length=20, verbose_name='닉네임')),
                ('created_at', models.DateField(verbose_name='리뷰일')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='책')),
            ],
            options={
                'verbose_name': '리뷰',
                'verbose_name_plural': '리뷰들',
            },
        ),
    ]
