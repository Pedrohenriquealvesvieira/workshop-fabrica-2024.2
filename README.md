# ❤️workshop-fabrica-2024.2
# Projeto Django

> [!NOTE]
> Este projeto Django gerencia `itens` e `localidades`, incluindo `modelos`, `serializers`, `views` e `URLs` para uma `API`.

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

#### Você poderá `criar` uma ou mais `Localidades` como por exemplo: "Garagem" e "Cozinha", as quais receberão um `ID` e o `Nome` que foi escolhido.

<div align="center">
<img src = "https://github.com/user-attachments/assets/e7eb3742-3df7-4d49-a9d7-53aca48ccdda" width="500px" />
</div>


### Detalhe da Localidade: 
> 🔗http://localhost:8000/api/localidade/id/

#### Ao especificar o `ID` na `URL` aparecerá apenas a Localidade que corresponde ao `ID` fornecido, nessa nova tela você poderá tanto `alterar` o `Nome` da `Localidade` como `removê-la` do banco de dados.

<div align="center">
<img src = "https://github.com/user-attachments/assets/2fa54c98-9289-4518-bacb-df040e967020" width="500px" />
</div>



### Lista de Itens: 
> 🔗http://localhost:8000/api/item/

#### Agora você poderá `criar` itens e adicioná-los as `Localidades` criadas previamente. Ao serem criados, os itens recebem um `ID`, o `Nome` escolhido, a `data de inclusão` desse item ano/mês/dia e a localidade que corresponde ao `ID` da Localidade a qual ela foi adicionada.

<div align="center">
<img src = "https://github.com/user-attachments/assets/c88c373a-e468-478c-94a0-e68911416cb6" width="500px" />
</div>

### Detalhe do Item: 
> 🔗http://localhost:8000/api/item/id/

#### Ao especificar o `ID` na `URL` aparecerá apenas o item que corresponde ao `ID` fornecido, nessa nova tela você poderá tanto `alterar` o `nome do item`, a sua `localidade` ou `removê-lo` do banco de dados.

<div align="center">
<img src = "https://github.com/user-attachments/assets/fda3d593-a717-4612-83cb-81990ecd40c8" width="500px" />
</div>

### Filtragem de Item:
> 🔗http://localhost:8000/api/item/?localidade=id/

#### Nesse caso ao adicionar item e especificar o `ID` da localidade na `URL` aparecerá apenas os item que estão na localidade correspondente ao `ID` fornecido, nessa nova tela você poderá `consultar` os itens da localidade desejada e também `alterar` a `Localidade` desse `Item`.

<div align="center">
<img src = "https://github.com/user-attachments/assets/5286d134-aaaa-4d11-8c7f-baa019d2236c" width="500px" />
</div>

# 🔚 7. Conclusão

#### Este projeto foi desenvolvido como parte de um desafio para ingressar no projeto de extensão `"Fábrica de Software"` da `faculdade`. A aplicação implementa um `CRUD` básico utilizando `Django` e `Django REST Framework`, demonstrando habilidades em desenvolvimento web, modelagem de dados, e criação de APIs RESTful. O objetivo principal foi criar uma solução funcional que permita gerenciar itens e localidades. 

#### gratidão aos instrutores.






