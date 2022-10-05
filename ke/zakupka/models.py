from django.db import models
from tovar.models import SKU, Tovar


class Zakup(models.Model):
    zakup_date = models.DateTimeField()
    course_USD = models.FloatField()  # Курс доллара к рублю
    course_CNY = models.FloatField()  # Курс Юаня к рублю


class Tovar_v_zakupku(models.Model):
    SKU = models.ForeignKey(SKU, on_delete=models.CASCADE, related_name='tovar_v_zakup')
    id_zakup = models.ForeignKey(Zakup, on_delete=models.CASCADE, related_name='tovar_v_zakup')
    price_in_china = models.FloatField()  # Цена закупки в китае в юанях
    kollichestvo = models.IntegerField()
    #ves = models.ForeignKey(SKU, on_delete=models.CASCADE, related_name='ves')
    price_delivery = models.FloatField()  # Стоимость доставки из китая в рублях
    name = models.ForeignKey(Tovar, on_delete=models.CASCADE, related_name='tovar_v_zakup')