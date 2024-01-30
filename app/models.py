from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    price = models.FloatField(max_length=100)

    def __str__(self) :
        return self.name
