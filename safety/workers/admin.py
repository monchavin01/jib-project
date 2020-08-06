from django.contrib import admin

from .models import Worker

@admin.register(Worker)
class WorkAdmin(admin.ModelAdmin):
    pass