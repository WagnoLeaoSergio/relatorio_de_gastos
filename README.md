## Descrição

O projeto de um Web App para monitoramento e registro de gastos diários que serão analisados através de um dashboard. Os dados inseridos serão armazenados em um banco de dados MongoDB.

## Requisitos

É necessário ter instalado no computador Python 3.6 ou superior.

## Instalação

Para instalar o Web App é necessário clonar o repositório, instalar as dependências especificadas no arquivo 'requirements.txt' e criar um novo arquivo na pasta raíz chamado '.env'. Nesse arquivo serão especificadas as variáveis `MONGO_DB_URI` e `choices`, que são o endereço URI do servidor MongoDB e as categorias de gastos a serem registradas, respectivamente.

É recomendável instalar o projeto dentro de um ambiente virtual.

## Execução

Para iniciar o Web App basta acessar pasta 'relatorio_de_gastos' e executar o comando `streamlit run main.py`.
