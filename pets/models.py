from django.db import models

# Create your models here.

class Pet(models.Model):

    TYPE_ANIMALS = (
        ("Gato", "Gato"),
        ("Perro", "Perro"),
        ("Pato", "Pato"),
        ("Tortuga", "Tortuga")
    )

    name = models.CharField(verbose_name="Name", max_length=50)
    age = models.SmallIntegerField(verbose_name="Age")
    type = models.CharField(verbose_name="Type", max_length=50, choices=TYPE_ANIMALS)

    def __str__(self):
        return self.name
    