# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models.car import Car
from .models.person import Person
from .models.scenario_rule import ScenarioRule
admin.site.register(Car)
admin.site.register(Person)
admin.site.register(ScenarioRule)

