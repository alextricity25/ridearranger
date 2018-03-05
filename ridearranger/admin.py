# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models.car import Car
from .models.person import Person
admin.site.register(Car)
admin.site.register(Person)
