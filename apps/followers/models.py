# coding: utf-8
from django.db import models


class Man(models.Model):
    name = models.CharField(max_length='225')
    follow_ids = models.TextField()
    follow = models.ManyToManyField(
        "self", symmetrical=False, related_name='followers', db_table='man_link')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "man_man"
