# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .car import Car

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    location = models.CharField(max_length = 20)
    is_driver = models.BooleanField(default=False)
    car = models.OneToOneField(
        Car,
        on_delete = models.CASCADE,
        blank = True,
        null = True
    )

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
