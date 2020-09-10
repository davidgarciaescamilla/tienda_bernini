# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models

# for create products


class Product(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.IntegerField()

    def __str__(self):
        return self.name
