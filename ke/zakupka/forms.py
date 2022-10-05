# from django import forms  # Импортируем модуль forms, из него возьмём класс ModelForm
#
# from .models import Tovar_v_zakupku  # Импортируем модель, чтобы связать с ней форму
#
# class BookForm(forms.ModelForm):
#     class Meta:
#         # Эта форма будет работать с моделью Book
#         model = Tovar_v_zakupku
#
#         # Здесь перечислим поля модели, которые должны отображаться в веб-форме;
#         # при необходимости можно вывести в веб-форму только часть полей из модели.
#         fields = ('name', 'isbn', 'pages')