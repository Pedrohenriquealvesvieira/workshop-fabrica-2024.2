from rest_framework import generics
from .models import Localidade, Item
from .serializers import ItemSerializer, LocalidadeSerializer

class ItemLista(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        queryset = Item.objects.all()
        localidade = self.request.query_params.get('localidade')
        if localidade is not None:
            queryset = queryset.filter(itemLocalidade=localidade)
        return queryset
    
class ItemDetalhe(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    
class LocalidadeLista(generics.ListCreateAPIView):
    serializer_class = LocalidadeSerializer
    queryset = Localidade.objects.all()
    
class LocalidadeDetalhe(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocalidadeSerializer
    queryset = Localidade.objects.all()
    
    
    

    
    