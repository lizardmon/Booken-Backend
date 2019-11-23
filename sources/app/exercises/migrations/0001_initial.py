# Generated by Django 2.2.7 on 2019-11-23 16:20

from django.db import migrations, models
import django.db.models.deletion
import exercises.models.exercise


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='이름')),
                ('calorie', models.IntegerField(blank=True, null=True, verbose_name='칼로리')),
                ('time', models.IntegerField(blank=True, null=True, verbose_name='시간')),
                ('power', models.CharField(blank=True, choices=[('weak', '약함'), ('normal', '보통'), ('strong', '강함')], max_length=255, null=True)),
            ],
            options={
                'verbose_name': '운동',
                'verbose_name_plural': '운동들',
            },
        ),
        migrations.CreateModel(
            name='ExerciseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='이름')),
                ('description', models.TextField(blank=True, verbose_name='설명')),
            ],
            options={
                'verbose_name': '운동 카테고리',
                'verbose_name_plural': '운동 카테고리들',
            },
        ),
        migrations.CreateModel(
            name='ExerciseImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.IntegerField(verbose_name='순서')),
                ('url', models.ImageField(upload_to=exercises.models.exercise.image_file_name, verbose_name='이미지')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.Exercise', verbose_name='운동')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainers.Trainer')),
            ],
            options={
                'verbose_name': '운동 이미지',
                'verbose_name_plural': '운동 이미지들',
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='ExerciseDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='운동 설명')),
                ('ordering', models.IntegerField(verbose_name='운동 정렬')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.Exercise')),
            ],
            options={
                'verbose_name': '운동 설명',
                'verbose_name_plural': '운동 설명들',
                'ordering': ['ordering'],
            },
        ),
        migrations.AddField(
            model_name='exercise',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.ExerciseCategory', verbose_name='카테고리'),
        ),
    ]
