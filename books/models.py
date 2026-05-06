from django.db import models
from genre.models import Genre
from writer.models import Writer

class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    book_genre = models.ForeignKey(Genre,on_delete=models.PROTECT, related_name='books')
    book_writers = models.ManyToManyField(Writer,related_name='writebook')

    def __str__(self):
        return self.name


