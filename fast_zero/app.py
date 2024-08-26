from http import HTTPStatus

from fastapi import FastAPI
import uvicorn

from fast_zero.routers import clientes
from fast_zero.schemas import Message

from front_nicegui import main


app = FastAPI()

# cd fast_zero
# poetry shell
# task run

# alembic init migrations
# ~change migrations/env.py if first time~
# alembic revision --autogenerate -m "create cliente table"
# alembic upgrade head

app.include_router(clientes.router)

main.init(app)

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'hello hello'}
