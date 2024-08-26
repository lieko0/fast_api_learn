# Fast API

Learning from [FastAPI do Zero by Dunossauro](https://fastapidozero.dunossauro.com/)

## Comandos para rodar

- Docker compose

``` shell
docker-compose up --build
```

- [Documentação da API](http://127.0.0.1:8000/docs/)
``` 
http://127.0.0.1:8000/docs/
```  

- [WIP] [Interface da API](http://127.0.0.1:8000/gui/) em [NiceGUI](https://nicegui.io/)
``` markdown
http://127.0.0.1:8000/gui/
```


## Comandos para o desenvolvimento

- Setup (python version = 3.12.* )
``` shell
pip install poetry
poetry install
```

- Ambiente virtual

``` sh
poetry shell
```


- Database

``` shell
docker-compose up -d fastzero_database
poetry run alembic upgrade head
```

```{toggle} 
:show:
.env
DATABASE_URL=postgresql+psycopg://{user}:{password}@{hostname}:{port}/{database-name}
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


