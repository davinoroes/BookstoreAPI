from django.contrib import admin
from genre.models import Genre

@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = ('name',)
