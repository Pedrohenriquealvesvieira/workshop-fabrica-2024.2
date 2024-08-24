from rest_framework import serializers
from .models import Item, Localidade


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')
        
class LocalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidade
        fields = ('__all__')