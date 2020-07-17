from django.db import models
from django.utils import timezone


def one_minute_hence():
    return timezone.now() - timezone.timedelta(minutes=1)


def one_day_hence():
    return timezone.now() - timezone.timedelta(days=1)


class Table(models.Model):
    color = models.CharField(max_length=10)
    number = models.CharField(max_length=2)
    date = models.DateTimeField(default=one_minute_hence)
    change_date = models.DateTimeField(default=one_day_hence)
    recom = models.CharField(max_length=10)
    do_date = models.DateTimeField()
