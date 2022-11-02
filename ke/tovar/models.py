from django.db import models


class Tovar(models.Model):
    tovar_link = models.URLField(max_length=500)  # Ссылка на товар в нашем магазине
    name = models.CharField(max_length=100)
    chaina_link = models.URLField(max_length=500)  # Ссылка на товар в китае
    opponents_link = models.TextField()  # Ссылка на конкурента
    slug = models.SlugField()  # название товара в системе
    photo = models.ImageField(null=True, blank=True)  # фото товара


class SKU(models.Model):
    id_tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE, related_name='id_tovar')
    razmer = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    image = models.ImageField()
    ves = models.FloatField()
    kolichestvo_na_sklade_marketplase = models.IntegerField()  # количество товара на маркетплейсах
    kolichestvo_na_sklade_home = models.IntegerField()  # количество товара на складах
