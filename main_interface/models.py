from django.db import models


class UserData(models.Model):
    balance = models.CharField(max_length=12, blank=False, default='0')
    volume = models.CharField(max_length=12, blank=False, default='0')
    results = models.CharField(max_length=12, blank=False, default='0')
    day_results = models.CharField(max_length=12, blank=False, default='0')
    previous_trade_id = models.CharField(max_length=60, blank=False, default='0')

    class Meta:
        verbose_name_plural = 'Users data'