from django.contrib import admin

from exercises.models import Exercise, ExerciseCategory, ExerciseImage


class ExerciseImageInlineAdmin(admin.StackedInline):
    model = ExerciseImage


@admin.register(ExerciseCategory)
class ExerciseCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    inlines = [
        ExerciseImageInlineAdmin,
    ]
