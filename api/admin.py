from django.contrib import admin

from .models import Localidade, Item

admin.site.register(Localidade) # Registra o modelo Localidade no admin
admin.site.register(Item) # Registra o modelo Item no admin
