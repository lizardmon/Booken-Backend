from django.contrib import admin

from trainers.models import Trainer


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    pass
