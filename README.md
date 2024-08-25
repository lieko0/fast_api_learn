# Fast API

Learning from [FastAPI do Zero by Dunossauro](https://fastapidozero.dunossauro.com/)

## Comandos para rodar

- Docker compose

``` shell
    docker-compose up --build
```

- Documentação da API
  
http://127.0.0.1:8000/docs/



## Comandos para o desenvolvimento

- Ambiente virtual

``` shell
    poetry shell
```


- Database

``` shell
    docker-compose up -d fastzero_database
```


- Atalhos

``` shell
task lint #= 'ruff check . && ruff check . --diff'

task format #= 'ruff check . --fix && ruff format .'

task run #= 'fastapi dev fast_zero/app.py'

task pre_test #= 'task lint'

task test = #'pytest -s -x --cov=fast_zero -vv'

task post_test #= 'coverage html'
```


