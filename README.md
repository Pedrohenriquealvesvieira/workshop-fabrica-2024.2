# ❤️workshop-fabrica-2024.2
# Projeto Django

> [!NOTE]
> Este projeto Django gerencia itens e localidades, incluindo modelos, serializers, views e URLs para uma API.

# 🔧 1. Instalação e Configuração

 - ## 🐍 1.1 Instalar Python
> [!IMPORTANT]
> Se você ainda não tem o Python instalado, baixe e instale a versão mais recente do Python a partir do [🔗site oficial](https://www.python.org/downloads/).


- ## ⚙️ 1.2 Configurar um Ambiente Virtual

> [!TIP]
> Para evitar conflitos de dependências, é recomendável usar um ambiente virtual. Siga os passos abaixo para criar e ativar um ambiente virtual.

#### 

 # ✨ 2. Crie um ambiente virtual
  - ### ✏️ digite o comando abaixo no terminal:

>🖥️ `python -m venv (nome) recomenda-se que o nome seja "venv" ou "env"`

- ## 🔌 2.1 Ative o ambiente virtual

  - ### ✏️ digite um dos comandos abaixo de acordo com seu sistema operacional no terminal:
#### No Windows

>🖥️ `venv\Scripts\activate`

#### No macOS/Linux
>🖥️ `source venv/bin/activate`

# 📦 3. Instalar as Dependências.
  
 - ## 💾 3.1 Com o ambiente virtual ativado, instale as dependências necessárias para o projeto.
    
  - ### ✏️digite o comando abaixo no terminal:
>🖥️ `pip install django djangorestframework`

# 🛠️ 4. Configurar o Projeto.

- ## ➕ 4.1 Criar Migrações: Gere os arquivos de migração para criar as tabelas no banco de dados.
  - ### ✏️ digite o comando abaixo no terminal:
>🖥️ `python manage.py makemigrations`

## ✅ Aplicar Migrações: Aplique as migrações para criar as tabelas no banco de dados.
  - ### ✏️ digite o comando abaixo no terminal:
>🖥️ `python manage.py migrate`

## ➕ Criar Superusuário: Crie um superusuário para acessar a interface administrativa do Django.
  - ### ✏️ digite o comando abaixo no terminal:
>🖥️ `python manage.py createsuperuser username (user) email (user@example.com)`

# 🚀 5. Executar o Servidor: Inicie o servidor Django para verificar o funcionamento da aplicação.
- ### ✏️ digite o comando abaixo no terminal:
> 🖥️ `python manage.py runserver`

- ## 🌐 5.1 Acesse o projeto no navegador em:
>🔗http://localhost:8000.

# 🧪 6. Testando a API

- ## 🧩 Funcionalidades: 

> [!CAUTION]
> **Atenção:** Dois itens ou duas localidades não podem ter o mesmo nome. O atributo `unique=True` no campo `localidadeNome` do modelo `Localidade` e no campo `itemNome` do modelo `Item` garante que cada nome seja único no banco de dados.

### Lista de Localidades: 
> 🔗http://localhost:8000/api/localidade/

#### Você poderá criar uma ou mais localidades como por exemplo: Garagem e Cozinha, as quais receberão um ID e o nome que foi escolhido.

### Detalhe da Localidade: 
> 🔗http://localhost:8000/api/localidade/id/

#### Ao especificar o ID na URL aparecerá apenas a localidade que corresponde ao ID fornecido, nessa nova tela você poderá tanto alterar o nome da localidade como removê-la do banco de dados.

### Lista de Itens: 
> 🔗http://localhost:8000/api/item/

#### Agora você poderá criar itens e adicioná-los as localidades criadas previamente. Ao serem criados, os itens recebem um ID, o nome escolhido, a data de inclusão desse item ano/mês/dia e a localidade que corresponde ao ID da Localidade a qual ela foi adicionada

### Detalhe do Item: 
> 🔗http://localhost:8000/api/item/id/

#### Ao especificar o ID na URL aparecerá apenas o item que corresponde ao ID fornecido, nessa nova tela você poderá tanto alterar o nome do item, a sua localidade ou removê-lo do banco de dados.

### Filtragem de Item:
> 🔗http://localhost:8000/api/item/?localidade=id/
> 
#### Nesse caso ao especificar o item e o ID da localidade na URL aparecerá apenas os item que corresponde estão localizados na localidade do ID fornecido, nessa nova tela você poderá consultar apenas os itens da localidade desejada.




