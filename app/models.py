from django.db import models
from category.models import Category


class Thumnails(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class Languages(models.Model):
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language


class App(models.Model):
    name = models.CharField(max_length=200, unique=True)
    company = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=2000)
    category = models.ForeignKey(Category)
    thumnails = models.URLField()
    des_thumnails = models.ForeignKey(Thumnails)
    language = models.ManyToManyField(Languages)
    rating = models.FloatField(default=3.0)
    store_url = models.URLField()
    last_update_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
