from django.contrib import admin

from .models import Tovar, SKU


class TovarAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('tovar_link', 'name', 'chaina_link', 'opponents_link')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('name',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class SKUAdmin(admin.ModelAdmin):
    list_display = ('razmer', 'color', 'image', 'ves')

    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Tovar, TovarAdmin)
