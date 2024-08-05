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
