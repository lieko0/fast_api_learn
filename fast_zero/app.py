from http import HTTPStatus

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fast_zero.routers import clientes
from fast_zero.schemas import Message

app = FastAPI()

# cd fast_zero
# poetry shell
# task run

# alembic init migrations
# ~change migrations/env.py if first time~
# alembic revision --autogenerate -m "create cliente table"
# alembic upgrade head

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clientes.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'hello hello'}
