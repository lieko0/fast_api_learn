# Fast API

Learning from [FastAPI do Zero by Dunossauro](https://fastapidozero.dunossauro.com/)

> [!IMPORTANT]
> Precisa de Docker e Docker Compose instalados

## Comandos para rodar

- Docker compose

``` shell
docker-compose up --build
```

- [Documentação da API](http://127.0.0.1:8000/docs/)

```
http://127.0.0.1:8000/docs/
```  

- [WIP] [Interface da API](http://127.0.0.1:8000/gui/) em [NextJS (react)](https://nextjs.org/)

``` markdown
http://127.0.0.1:8000/gui/
```

<br>

## Comandos para o desenvolvimento

> [!IMPORTANT]
> Precisa de Python versão 3.12.* instalado

- Setup

``` shell
pip install poetry
```

- Ambiente virtual & Instalação de dependências

``` sh
cd .\fast_api_learn\
poetry shell
poetry install
```

- Criar arquivo de variáveis

<details>
  <summary>.env</summary>
  DATABASE_URL=postgresql+psycopg://{user}:{password}@{hostname}:{port}/{database-name}
</details>

- Iniciar e configurar o Banco de Dados

``` shell
docker-compose up -d fastzero_database
poetry run alembic upgrade head
```

- Rodar a aplicação

``` shell
task run
```

- Parar o banco de dados

``` shell
docker-compose down
```

- Outros atalhos

``` shell
task lint # Roda o lint e verifica problemas na formatação

task format # Formata (quase tudo) de acordo com o padrão e mostra o que precisa ser formatado na mão

task run # Roda a aplicação com o comando 'fastapi dev'

task pre_test # Verifica o lint antes de realizar os testes

task test = # Roda todos os teste da API do backend pelo pytest

task post_test # Apresenta o 'coverage html'
```
