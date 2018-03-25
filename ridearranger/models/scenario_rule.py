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
    GROUP_BY_CHOICES = {
        ('dest', 'Destination Location'),
        ('src', 'Source Location')
    }

    name = models.CharField(
        max_length = 20
    )
    source_location_rule = models.CharField(
        max_length = 20,
        choices = SOURCE_LOCATION_RULE_CHOICES
    )
    dest_location_rule = models.CharField(
        max_length = 20,
        choices = DEST_LOCATION_RULE_CHOICES
    )
    group_by_rule = models.CharField(
        max_length = 20,
        choices = GROUP_BY_CHOICES 
    )
    def __str__(self):
        return "{}".format(self.name)
