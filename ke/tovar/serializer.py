
from rest_framework import serializers

from .models import Tovar, SKU


class TovarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tovar
        fields = ('tovar_link', 'name', 'chaina_link', 'opponents_link', 'slug')


class SKUSerializer(serializers.ModelSerializer):

    class Meta:
        model = SKU
        fields = ('id_tovar', 'razmer','color', 'image', 'ves', 'kolichestvo_na_sklade_marketplase', 'kolichestvo_na_sklade_home')