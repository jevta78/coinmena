from django.db import models


class BtcUsd(models.Model):
    from_currency_code = models.CharField(max_length=5)
    to_currency_code = models.CharField(max_length=5)
    exchange_rate = models.FloatField()
    date = models.DateTimeField()
    time_zone = models.CharField(max_length=5)
    bid_price = models.FloatField()
    ask_price = models.FloatField()

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'{self.from_currency_code} / {self.to_currency_code}'
