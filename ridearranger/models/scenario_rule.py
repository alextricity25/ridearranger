# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ScenarioRule(models.Model):

    SOURCE_LOCATION_RULE_CHOICES = (
        ('HL', 'Home Location'),
        ('SL', 'Same Location')
    )
    DEST_LOCATION_RULE_CHOICES = (
        ('HL', 'Home Location'),
        ('SL', 'Same Location')
    )

    source_location_rule = models.CharField(
        max_length = 20,
        choices = SOURCE_LOCATION_RULE_CHOICES
    )
    dest_location_rule = models.CharField(
        max_length = 20,
        choices = DEST_LOCATION_RULE_CHOICES
    )
    name = models.CharField(
        max_length = 20
    )

    def __str__(self):
        return "{}".format(self.name)
