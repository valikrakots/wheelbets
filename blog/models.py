from django.db import models
from django.utils import timezone


def one_minute_hence():
    return timezone.now() - timezone.timedelta(minutes=1)


def one_day_hence():
    return timezone.now() - timezone.timedelta(days=1)


class Table(models.Model):
    da = models.CharField(max_length=10)
