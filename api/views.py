from rest_framework import generics
from .models import Localidade, Item
from .serializers import ItemSerializer, LocalidadeSerializer

class ItemLista(generics.ListCreateAPIView):  # View para lista e criação de itens
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        queryset = Item.objects.all()
        localidade = self.request.query_params.get('localidade')
        if localidade is not None:
            queryset = queryset.filter(itemLocalidade=localidade) # Filtrando por localidade
        return queryset
    
class ItemDetalhe(generics.RetrieveUpdateDestroyAPIView): # View para detalhe, atualização e exclusão de itens
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    
class LocalidadeLista(generics.ListCreateAPIView): # View para lista e criação de localidades
    serializer_class = LocalidadeSerializer
    queryset = Localidade.objects.all()
    
class LocalidadeDetalhe(generics.RetrieveUpdateDestroyAPIView): # View para detalhe, atualização e exclusão de localidades
    serializer_class = LocalidadeSerializer
    queryset = Localidade.objects.all()
    
    
    

    
    