from django.db import models
from tovar.models import Tovar, SKU


class Zakaz(models.Model):
    STATUS_CHOICES = [
        ('В обработке', 'В обработке'),
        ('Отменено', 'Отменено'),
        ('Доставлен', 'Доставлен')
    ]

    create_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    arrive_date = models.DateTimeField()
    price = models.FloatField()


class Tovar_v_zakaze(models.Model):
    id_zakaza = models.ForeignKey(Zakaz, on_delete=models.CASCADE, related_name='tovary')
    id_tovara = models.ForeignKey(Tovar, on_delete=models.CASCADE, related_name='zakazy')
    count = models.IntegerField()
    price = models.FloatField()
    commission = models.IntegerField()
    SKU = models.ForeignKey(SKU, on_delete=models.CASCADE, related_name='zakazy')
