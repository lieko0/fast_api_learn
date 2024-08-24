# Fast API

Learning from [FastAPI do Zero by Dunossauro](https://fastapidozero.dunossauro.com/)

## Comandos

- Ambiente virtual

``` shell
    poetry shell
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


docker run -d --name app_database -e POSTGRES_USER=app_user -e POSTGRES_DB=app_db -e POSTGRES_PASSWORD=app_password -v pgdata:/var/lib/postgresql/data -p 5432:5432 postgres