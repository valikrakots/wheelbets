from django.db import models
from django.utils import timezone


def one_minute_hence():
    return timezone.now() - timezone.timedelta(minutes=1)


def one_day_hence():
    return timezone.now() - timezone.timedelta(days=1)


class Table(models.Model):
    previous = models.CharField(max_length=7)
    number = models.CharField(max_length=2)
    date = models.DateTimeField(default=one_minute_hence)
    change_date = models.DateTimeField(default=one_day_hence)
    success = models.CharField(max_length=7)
    recom = models.CharField(max_length=7)
    str = models.TextField(max_length=10000000000)

class TableImage(models.Model):
    firsttime = models.DateTimeField(default=timezone.now())

