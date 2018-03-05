# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length = 20)
    make = models.CharField(max_length = 20)
    year = models.CharField(max_length = 4)
    num_passengers = models.IntegerField()



    def __str__(self):
        return self.name
    
