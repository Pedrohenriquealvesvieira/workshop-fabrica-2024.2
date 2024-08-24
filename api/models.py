from django.db import models # Importando models

class Localidade(models.Model): # Modelo para Localidade
    localidadeNome = models.CharField(max_length=100, unique=True) # Nome da localidade
    
    def __str__(self):
        return self.localidadeNome # Representação em string
    
class Item(models.Model): # Modelo para Item
    itemNome = models.CharField(max_length=100) # Nome do item
    dataInclusao = models.DateField(auto_now_add=True) # Data de inclusão automática
    itemLocalidade = models.ForeignKey(Localidade, on_delete=models.CASCADE) # Referência para Localidade
    
    def __str__(self):
        return self.itemNome # Representação em string

'''
*Explicação dos parâmetros utilizados:

-O parâmetro on_delete é usado em campos de tipo 'ForeignKey' para definir o comportamento do banco de dados quando o objeto relacionado é excluído.

-O parâmetro unique=True é usado para garantir que os valores nesse campo sejam únicos em toda a tabela do banco de dados.

-O parâmetro auto_now_add é usado em campos do tipo DateField, o Django preenche automaticamente esse campo com a data e a hora atuais no momento em que o registro é criado.

-O parâmetro max_length é usado para definir o comprimento máximo permitido para o valor armazenado nesse campo.
'''