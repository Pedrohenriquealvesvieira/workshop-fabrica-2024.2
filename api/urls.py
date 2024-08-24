from django.urls import path
from .views import ItemLista, ItemDetalhe, LocalidadeLista, LocalidadeDetalhe # Importando views

urlpatterns = [
      path('item/', ItemLista.as_view()),
      path('item/<int:pk>/', ItemDetalhe.as_view()),
      path('localidade/', LocalidadeLista.as_view()),
      path('localidade/<int:pk>/', LocalidadeDetalhe.as_view()), 
                
]
