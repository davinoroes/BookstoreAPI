from django.db import models

NATIONALITY_CHOICES = (('BR', 'Brasil'),
                       ('USA','Estados Unidos'),
                       ('PT','Portugal'),
                       ('DE', 'Alemanha'),
                       ('FR', 'Franca'),
                       ('UK', 'Reino Unido'),)

class Writer(models.Model):
    name = models.CharField(max_length=50)
    nationality = models.CharField(choices=NATIONALITY_CHOICES)

    def __str__(self):
        return self.name

