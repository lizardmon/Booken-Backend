# Generated by Django 2.2.7 on 2019-11-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='english_name',
            field=models.CharField(default='', max_length=255, verbose_name='영어 이름'),
            preserve_default=False,
        ),
    ]
