from django.contrib import admin
from books.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','price','book_genre',)