# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


# for registers users

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# for create a products

class Product(models.Model):
    cliente = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title
