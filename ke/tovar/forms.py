from django import forms  # Импортируем модуль forms, из него возьмём класс ModelForm

from .models import Tovar, SKU  # Импортируем модель, чтобы связать с ней форму


class TovarForm(forms.ModelForm):
    class Meta:
        model = Tovar

        fields = ('tovar_link', 'name', 'chaina_link', 'opponents_link', 'slug')


class SKUForm(forms.ModelForm):
    class Meta:
        model = SKU

        fields = '__all__'
