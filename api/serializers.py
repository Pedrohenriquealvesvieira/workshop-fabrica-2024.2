from rest_framework import serializers
from .models import Item, Localidade #importando modelos


class ItemSerializer(serializers.ModelSerializer): # Serializer para Item
    class Meta:
        model = Item
        fields = ('__all__')
        
class LocalidadeSerializer(serializers.ModelSerializer): # Serializer para Localidade
    class Meta:
        model = Localidade
        fields = ('__all__')
    
'''
O '__all__' é utilizado para que ele inclua todos os campos
'''