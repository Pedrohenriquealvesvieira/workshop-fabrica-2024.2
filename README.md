# ❤️workshop-fabrica-2024.2

# Projeto Django
> Este projeto Django gerencia itens e localidades, incluindo modelos, serializers, views e URLs para uma API.

# 🔧Instalação e Configuração

## 🐍1. Instalar Python

Se você ainda não tem o Python instalado, baixe e instale a versão mais recente do Python a partir do [🔗site oficial](https://www.python.org/downloads/).

## 2. Configurar um Ambiente Virtual

### Para evitar conflitos de dependências, é recomendável usar um ambiente virtual. Siga os passos abaixo para criar e ativar um ambiente virtual.

# Crie um ambiente virtual

>🖥️ python -m venv venv

## Ative o ambiente virtual

### No Windows

>🖥️ venv\Scripts\activate

### No macOS/Linux
>🖥️ source venv/bin/activate

# 📦Instalar as Dependências.

## Com o ambiente virtual ativado, instale as dependências necessárias para o projeto.
>🖥️ pip install django djangorestframework

# 🛠️Configurar o Projeto.

## Criar Migrações: Gere os arquivos de migração para criar as tabelas no banco de dados.
>🖥️ python manage.py makemigrations

## Aplicar Migrações: Aplique as migrações para criar as tabelas no banco de dados.
>🖥️ python manage.py migrate

## Criar Superusuário: Crie um superusuário para acessar a interface administrativa do Django.
>🖥️ python manage.py createsuperuser username (user) email (user@example.com)

# 🚀Executar o Servidor: Inicie o servidor Django para verificar o funcionamento da aplicação.
>🖥️ python manage.py runserver

## Acesse o projeto no navegador em
>🔗http://localhost:8000.

# 🧪Testando a API

## Lista de Localidades: 
> 🔗http://localhost:8000/api/localidade/

### Você poderá criar uma ou mais localidades como por exemplo: Garagem e Cozinha, as quais receberão um ID e o nome que foi escolhido.(Não poderá existir duas localidades com o mesmo nome).

## Detalhe da Localidade: 
> 🔗http://localhost:8000/api/localidade/id/

### Ao especificar o ID na URL aparecerá apenas a localidade que corresponde ao ID fornecido, nessa nova tela você poderá tanto alterar o nome da localidade como removê-la do banco de dados.

## Lista de Itens: 
> 🔗http://localhost:8000/api/item/

### Agora você poderá criar itens e adicioná-los as localidades criadas previamente. Ao serem criados, os itens recebem um ID, o nome escolhido, a data de inclusão desse item ano/mês/dia e a localidade que corresponde ao ID da Localidade a qual ela foi adicionada

## Detalhe do Item: 
> 🔗http://localhost:8000/api/item/id/

### Ao especificar o ID na URL aparecerá apenas o item que corresponde ao ID fornecido, nessa nova tela você poderá tanto alterar o nome do item, a sua localidade ou removê-lo do banco de dados.

## Filtragem de Item:
> 🔗http://localhost:8000/api/item/?localidade=id/
> 
### Nesse caso ao especificar o item e o ID da localidade na URL aparecerá apenas os item que corresponde estão localizados na localidade do ID fornecido, nessa nova tela você poderá consultar apenas os itens da localidade desejada.




