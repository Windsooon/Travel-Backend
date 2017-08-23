from django.db import models
from category.models import Category


class Country(models.Model):
    name = models.CharField(max_length=200, unique=True)
    position = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
    thumnails = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
