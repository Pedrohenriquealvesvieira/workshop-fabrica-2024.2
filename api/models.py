from django.db import models

class Localidade(models.Model):
    localidadeNome = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.localidadeNome
    
class Item(models.Model):
    itemNome = models.CharField(max_length=100)
    dataInclusao = models.DateField(auto_now_add=True)
    itemLocalidade = models.ForeignKey(Localidade, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.itemNome
